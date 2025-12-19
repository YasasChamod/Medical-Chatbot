import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify

from langchain_pinecone import PineconeVectorStore
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain

from src.helper import download_embeddings
from src.prompt import system_prompt

# -------------------------
# Load env
# -------------------------
load_dotenv()

app = Flask(__name__)

# -------------------------
# Embeddings
# -------------------------
embeddings = download_embeddings()

# -------------------------
# Vector Store
# -------------------------
docsearch = PineconeVectorStore.from_existing_index(
    index_name="medical-chatbot",
    embedding=embeddings
)

retriever = docsearch.as_retriever(search_kwargs={"k": 3})

# -------------------------
# Groq LLM
# -------------------------
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}")
    ]
)

qa_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, qa_chain)

# -------------------------
# Routes
# -------------------------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    query = data.get("question", "")

    if not query:
        return jsonify({"answer": "Please ask a medical question."})

    response = rag_chain.invoke({"input": query})
    return jsonify({"answer": response["answer"]})

# -------------------------
# Run App
# -------------------------
if __name__ == "__main__":
    app.run(debug=True)
