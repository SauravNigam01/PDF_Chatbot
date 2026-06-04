from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

# Load embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load vector database
db = FAISS.load_local(
    "vectorstore",
    embeddings,
    allow_dangerous_deserialization=True
)

while True:
    query = input("\nAsk a question (or type 'exit'): ")

    if query.lower() == "exit":
        break

    docs = db.similarity_search(query, k=3)

    print("\nRelevant Context:\n")
    for i, doc in enumerate(docs, start=1):
        print(f"--- Chunk {i} ---")
        print(doc.page_content)
        print()