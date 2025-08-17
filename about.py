import streamlit as st

class About:
    @staticmethod
    def about():
        st.title("About This App")

        st.markdown("""
        **Custom Chat & Knowledgebase App** 🧠

        This application allows you to:
        - **Upload PDFs or text files** and chat with them directly.
        - **Ingest documents** into a Pinecone knowledge base for future queries.
        - **Query a knowledge base** with natural language questions.

        **Technologies Used:**
        - Streamlit for the web interface
        - LangChain for LLM and vector store integration
        - HuggingFace embeddings
        - FAISS (for temporary in-memory vector store)
        - Pinecone for scalable knowledge base

        **Author:** Ahmed Bin Mazhar ([@ahmedbinmazhar])  
        **Version:** 1.0
        """)

        st.info("This app is for demo and research purposes. Always verify critical responses from AI models.")
