# 📄 PDF Chatbot (RAG using LangGraph + FAISS + Hugging Face)

A Retrieval-Augmented Generation (RAG) based AI chatbot that allows users to query PDF documents and get intelligent answers.  
Built using **LangGraph, FAISS, Hugging Face embeddings, and Streamlit**.

---

## 🚀 Features

- 📄 Load and process PDF documents
- ✂️ Text splitting using RecursiveCharacterTextSplitter
- 🔎 Semantic search using FAISS vector database
- 🤖 Hugging Face embeddings (`all-MiniLM-L6-v2`)
- 🧠 LLM-based response generation (TinyLlama / HF models)
- 🔗 LangGraph workflow orchestration
- 💬 Streamlit chatbot interface

---

## 🏗️ Architecture

PDF Document  
⬇  
PDF Loader (PyPDFLoader)  
⬇  
Text Splitting (Chunking)  
⬇  
Embeddings (Hugging Face)  
⬇  
FAISS Vector Store  
⬇  
Retriever (Similarity Search)  
⬇  
LLM (Hugging Face Model)  
⬇  
Final Answer

---

## 📁 Project Structure
# PDF_Chatbot

**PDF Chatbot (RAG) **
│
├── app.py # Streamlit UI
├── graph.py # LangGraph workflow
├── ingest.py # PDF processing + vector DB creation
├── chat.py # CLI chatbot (optional)
├── check.py # Debug script
│
├── docs/
│ └── SauravnigamResume.pdf
│
└── vectorstore/
├── index.faiss
└── index.pkl


