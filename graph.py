from typing import TypedDict
from langgraph.graph import StateGraph, END
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from transformers import pipeline


class State(TypedDict):
    question: str
    context: str
    answer: str


# Load embeddings + vector DB (OK at startup)
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = FAISS.load_local(
    "vectorstore",
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = db.as_retriever(search_kwargs={"k": 3})


def get_llm():
    return pipeline(
        "text-generation",
        model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
        max_new_tokens=200,
    )


def retrieve(state):
    docs = retriever.invoke(state["question"])
    context = "\n\n".join([d.page_content for d in docs])
    return {"context": context}


def generate(state):
    llm = get_llm()

    prompt = f"""
You are a helpful AI assistant.

Context:
{state['context']}

Question:
{state['question']}

Answer in clear and complete sentences:
"""

    response = llm(
        prompt,
        max_new_tokens=256,
        do_sample=True,
        temperature=0.2,
        return_full_text=False   # ⭐ IMPORTANT FIX
    )

    return {"answer": response[0]["generated_text"]}

  


builder = StateGraph(State)

builder.add_node("retrieve", retrieve)
builder.add_node("generate", generate)

builder.set_entry_point("retrieve")
builder.add_edge("retrieve", "generate")
builder.add_edge("generate", END)

graph = builder.compile()