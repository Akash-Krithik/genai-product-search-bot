from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings

def get_vectorstore():
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return Chroma(persist_directory="db", embedding_function=embeddings)
