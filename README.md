# Confidential Offline RAG Chatbot

A fully offline Retrieval-Augmented Generation (RAG) chatbot built for defense-sector use cases. Supports secure Q&A over sensitive documents using an embedded LLM model (Mistral 7B) with FAISS indexing and local PDF ingestion.

## Features
- 🔐 Offline LLM (no internet dependency)
- 📄 PDF ingestion and chunking
- 🔍 FAISS similarity search
- 💬 Streamlit UI for local interaction

## Stack
- Python
- GPT4All (offline)
- FAISS
- SentenceTransformers
- Streamlit

> Designed during internship at Ordnance Factory, India (July 2025)

1. Prerequisites
- Python 3.10 or higher installed- Visual Studio Code (VSCode) installed- Git installed (optional but recommended)- Internet connection for downloading dependencies

2. Project Setup in VSCode
1. Open VSCode.
2. Install the 'Python' extension by Microsoft.
3. Open the project folder in VSCode: File > Open Folder
4. Create a virtual environment:   - On Windows: `python -m venv venv`   - On macOS/Linux: `python3 -m venv venv`
5. Activate the virtual environment:   - Windows: `venv\Scripts\activate`   - macOS/Linux: `source venv/bin/activate`

3. Installing Dependencies
1. Make sure you're in the activated virtual environment.2. Run the following command to install required packages:   - `pip install -r requirements.txt`

4. Running the Project
1. Make sure the virtual environment is activated.
2. Run the commands - python embed_and_index.py and streamlit run app.py after uploading the relevent files in data folder named as sample_manual.pdf.

