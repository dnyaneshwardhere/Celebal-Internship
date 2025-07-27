# vector_store.py
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from prepare import create_documents

def create_vector_store():
    documents = create_documents()
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db = FAISS.from_documents(documents, embeddings)
    db.save_local("vectorstore")
    return db

if __name__ == "__main__":
    create_vector_store()
