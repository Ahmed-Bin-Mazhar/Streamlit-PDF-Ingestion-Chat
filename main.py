import streamlit as st
from about import About
from chat import Chatbot
from ingestion import Ingestion
from knowledgebase import KnowledgebaseChat
from streamlit_option_menu import option_menu


with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Ingestion", "Chat Custom File", "Chat Knowledgebase", "About"],
        icons=["cloud-upload", "Chat", "info-circle"],
        menu_icon="cast",
        default_index=0,
    )

# Display content based on the selected option
if selected == "Ingestion":
    Ingestion.ingestion()

elif selected == "Chat Custom File":
    Chatbot.chatbot()

elif selected == "Chat Knowledgebase":
    KnowledgebaseChat.chat()
    print("[+] Do your Retriver code ")

elif selected == "About":
    About.about()
