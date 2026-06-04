import streamlit as st
from graph import graph

st.title("PDF Chatbot")

question = st.text_input(
    "Ask a question about your PDF"
)

if question:

    result = graph.invoke(
        {
            "question": question,
            "context": "",
            "answer": ""
        }
    )

    st.write(result["answer"])