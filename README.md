# Streamlit Chatbot Application

A powerful PDF-based chatbot application built with Streamlit, LangChain, and Groq LLM. This application allows users to upload PDF documents and interact with them through natural language conversations.

## 🚀 Features

- **PDF Document Processing**: Upload and process PDF files
- **Intelligent Chat Interface**: Natural language conversations with your documents
- **Vector-based Search**: FAISS vector store for efficient document retrieval
- **Advanced LLM Integration**: Powered by Groq's Llama 3.3 70B model
- **Real-time Chat**: Interactive chat interface with message history
- **Document Embedding**: Sentence transformers for semantic understanding

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **LLM**: Groq (Llama 3.3 70B Versatile)
- **Embeddings**: HuggingFace Sentence Transformers
- **Vector Store**: FAISS
- **PDF Processing**: PyPDF2
- **Framework**: LangChain

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.13 or higher**
- **Git** (for cloning the repository)
- **Groq API Key** (free account available at [groq.com](https://groq.com))

## 🚀 Installation & Setup

### Step 1: Clone the Repository

```bash
git clone <your-repository-url>
cd chatbot_streamlitapp
```

### Step 2: Create Virtual Environment

#### Option A: Using Python venv (Recommended)
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

#### Option B: Using uv (Fast Python Package Manager)
```bash
# Install uv if you haven't already
pip install uv

# Create and activate virtual environment
uv venv
uv sync
```

### Step 3: Install Dependencies

```bash
# Install all required packages
pip install -r requirements.txt
```

### Step 4: Environment Configuration

1. **Copy the environment sample file:**
   ```bash
   cp .env-sample .env
   ```

2. **Edit the `.env` file with your API keys:**
   ```env
   GROQ_LLM_MOODEL="llama-3.3-70b-versatile"
   EMBED_MODEL_NAME="sentence-transformers/all-MiniLM-L6-v2"
   GROQ_API_KEY="your-groq-api-key-here"
   ```

3. **Get your Groq API Key:**
   - Visit [groq.com](https://groq.com)
   - Sign up for a free account
   - Navigate to API Keys section
   - Create a new API key
   - Copy and paste it into your `.env` file

### Step 5: Run the Application

You have several options to run the application:

#### Option A: Using app.py (Recommended)
```bash
# Run using the app.py entry point
python app.py
```

#### Option B: Using streamlit run directly
```bash
# Start the Streamlit application directly
streamlit run main.py
```

#### Option C: Using streamlit run with app.py
```bash
# Alternative way to run the application
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

## 📖 Usage Guide

### 1. Upload a PDF Document
- Click on "Choose a file" button
- Select a PDF document from your computer
- The application will automatically process and embed the document

### 2. Start Chatting
- Once the PDF is uploaded, you'll see a chat interface
- Type your questions in the chat input box
- The chatbot will search through your document and provide relevant answers

### 3. Example Questions
- "What is the main topic of this document?"
- "Summarize the key points"
- "What are the conclusions?"
- "Explain the methodology used"

## 🔧 Configuration Options

### Model Configuration
You can modify the following parameters in the `.env` file:

- **GROQ_LLM_MOODEL**: The LLM model to use (default: "llama-3.3-70b-versatile")
- **EMBED_MODEL_NAME**: The embedding model for document processing
- **GROQ_API_KEY**: Your Groq API key

### Application Settings
In `main.py`, you can adjust:

- **Chunk Size**: Modify `chunk_size` in the text splitter (default: 500)
- **Chunk Overlap**: Modify `chunk_overlap` in the text splitter (default: 50)
- **Temperature**: Adjust LLM creativity (default: 0 for factual responses)

## 📁 Project Structure

```
chatbot_streamlitapp/
├── main.py              # Main application file
├── app.py               # Application entry point
├── requirements.txt     # Python dependencies
├── pyproject.toml      # Project configuration
├── .env-sample         # Environment variables template
├── .env                # Your environment variables (create this)
├── README.md           # This documentation
└── .venv/              # Virtual environment directory
```

## 🐛 Troubleshooting

### Common Issues

1. **ModuleNotFoundError**: Ensure your virtual environment is activated
   ```bash
   .venv\Scripts\activate  # Windows
   source .venv/bin/activate  # macOS/Linux
   ```

2. **API Key Error**: Verify your Groq API key is correctly set in the `.env` file

3. **Port Already in Use**: If port 8501 is busy, Streamlit will automatically use the next available port

4. **PDF Processing Issues**: Ensure the PDF is not corrupted and contains extractable text

### Performance Tips

- **Large PDFs**: For very large documents, consider increasing chunk size
- **Memory Usage**: The application loads the entire document into memory
- **API Limits**: Be mindful of Groq API rate limits

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) for the web framework
- [LangChain](https://langchain.com/) for the LLM framework
- [Groq](https://groq.com/) for the LLM API
- [HuggingFace](https://huggingface.co/) for the embedding models
- [FAISS](https://github.com/facebookresearch/faiss) for vector storage

## 📞 Support

If you encounter any issues or have questions:

1. Check the troubleshooting section above
2. Review the [Streamlit documentation](https://docs.streamlit.io/)
3. Check [Groq documentation](https://console.groq.com/docs)
4. Open an issue in the repository

---

**Happy Chatting! 🚀**
