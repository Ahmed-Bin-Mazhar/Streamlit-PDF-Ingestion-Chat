import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.chains.question_answering import load_qa_chain
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Pinecone as PineconeVectorStore
from pinecone import Pinecone

load_dotenv()

embedding_model = HuggingFaceEmbeddings(model_name=os.environ.get("EMBED_MODEL_NAME"))

# Pinecone setup
pc = Pinecone(api_key=os.environ.get("PINECONE_API_KEY"))
INDEX_NAME = os.environ["PINECONE_INDEX"]

# LLM
llm = ChatGroq(
    temperature=0,
    model_name=os.environ.get("GROQ_LLM_MODEL"),
)

class KnowledgebaseChat:
    @staticmethod
    def chat():
        st.title("Chat With Your Knowledgebase")

        if INDEX_NAME not in pc.list_indexes().names():
            st.warning("⚠️ No Pinecone index found. Please ingest documents first.")
            return

        # Connect to Pinecone index
        db = PineconeVectorStore.from_existing_index(INDEX_NAME, embedding_model)
        qa = load_qa_chain(llm=llm, chain_type="stuff")

        if "messages" not in st.session_state:
            st.session_state.messages = []

        for message in st.session_state["messages"]:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        if user_prompt := st.chat_input("Ask about your knowledgebase..."):
            st.chat_message("user").markdown(user_prompt)
            st.session_state.messages.append({"role": "user", "content": user_prompt})

            retriever = db.similarity_search(user_prompt, k=3)
            response = qa.invoke({"input_documents": retriever, "question": user_prompt})

            with st.chat_message("assistant"):
                st.markdown(response["output_text"])

            st.session_state.messages.append(
                {"role": "assistant", "content": response["output_text"]}
            )
