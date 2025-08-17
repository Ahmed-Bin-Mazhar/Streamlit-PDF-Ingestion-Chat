import streamlit as st
from about import About
from chat import Chatbot
from ingestion import Ingestion
from knowledgebase import KnowledgebaseChat
from streamlit_option_menu import option_menu

# Initialize session state for previous tab
if "prev_tab" not in st.session_state:
    st.session_state.prev_tab = None

# Initialize chat messages if not present
if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Ingestion", "Chat Custom File", "Chat Knowledgebase", "About"],
        icons=["cloud-upload", "chat-dots", "database", "info-circle"],
        menu_icon="cast",
        default_index=0,
    )

# Clear chat messages if user switches tabs
if st.session_state.prev_tab != selected:
    st.session_state.messages = []
    st.session_state.prev_tab = selected

# Display content based on the selected option
if selected == "Ingestion":
    Ingestion.ingestion()

elif selected == "Chat Custom File":
    Chatbot.chatbot()

elif selected == "Chat Knowledgebase":
    KnowledgebaseChat.chat()

elif selected == "About":
    About.about()
