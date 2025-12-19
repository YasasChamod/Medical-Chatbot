import os
from dotenv import load_dotenv

from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore

from src.helper import (
    load_pdf_files,
    filter_to_minimal_docs,
    text_split,
    download_embeddings
)

# Load env
load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

# Process data
documents = load_pdf_files("data")
documents = filter_to_minimal_docs(documents)
chunks = text_split(documents)

embeddings = download_embeddings()

# Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)
index_name = "medical-chatbot"

if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )

# Store vectors
PineconeVectorStore.from_documents(
    documents=chunks,
    embedding=embeddings,
    index_name=index_name
)

print("✅ Pinecone index created and data stored")
