import os
import streamlit as st
import PyPDF2
from dotenv import load_dotenv
from langchain.text_splitter import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Pinecone as PineconeVectorStore
from pinecone import Pinecone, ServerlessSpec

load_dotenv()

# Embeddings
embedding_model = HuggingFaceEmbeddings(model_name=os.environ.get("EMBED_MODEL_NAME"))

# Pinecone setup
pc = Pinecone(api_key=os.environ.get("PINECONE_API_KEY"))
INDEX_NAME = os.environ["PINECONE_INDEX"]

# Create index if not exists
if INDEX_NAME not in pc.list_indexes().names():
    pc.create_index(
        name=INDEX_NAME,
        dimension=384,   # must match your embedding model (e.g., 384 for MiniLM)
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )

class Ingestion:
    @staticmethod
    def read_pdf(pdf_file):
        reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text

    @staticmethod
    def ingestion():
        st.title("Upload Your Document!")

        uploaded_file = st.file_uploader("Choose a file", type=["pdf", "txt"])

        if uploaded_file:
            # Extract text
            if uploaded_file.type == "application/pdf":
                text = Ingestion.read_pdf(uploaded_file)
            else:
                text = uploaded_file.read().decode("utf-8")

            # Split text into chunks
            splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
            chunks = splitter.split_text(text)

            # Connect to LangChain Pinecone wrapper
            db = PineconeVectorStore.from_existing_index(INDEX_NAME, embedding_model)

            # Add new texts
            db.add_texts(chunks)

            st.success("✅ Document ingested and stored in Pinecone!")
