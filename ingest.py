from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

loader = PyPDFLoader("docs/SauravnigamResume.pdf")

docs = loader.load()
print("PDF loaded")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = splitter.split_documents(docs)
print(f"Created {len(chunks)} chunks")

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
print("Embeddings model loaded")

db = FAISS.from_documents(chunks, embeddings)
print("FAISS index created")

db.save_local("vectorstore")
print("Vectorstore saved successfully")