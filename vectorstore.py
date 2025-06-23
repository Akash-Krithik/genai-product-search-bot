# vectorstore.py

import os
import pandas as pd
from langchain_core.documents import Document
from langchain_text_splitters import CharacterTextSplitter
# Import FAISS instead of Chroma
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# Define the path for the FAISS index
DB_FAISS_PATH = "faiss_index"
DATA_PATH = "data/electrical_products.csv"

def get_vectorstore():
    """
    Initializes and returns a FAISS vector store.
    If the index doesn't exist on disk, it creates it and ingests data.
    """
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    if os.path.exists(DB_FAISS_PATH):
        print("✅ FAISS index found on disk. Loading...")
        # The allow_dangerous_deserialization flag is required for FAISS
        db = FAISS.load_local(
            DB_FAISS_PATH, embeddings, allow_dangerous_deserialization=True
        )
    else:
        print("ℹ️ FAISS index not found. Creating and ingesting data now...")
        df = pd.read_csv(DATA_PATH)
        
        texts = []
        for _, row in df.iterrows():
            content = f"Brand: {row['brand']}, Product: {row['product']}, Color: {row['color']}, Price: ₹{row['price']}, Offer: {row['offer_percent']}%"
            texts.append(Document(page_content=content))

        splitter = CharacterTextSplitter(separator="\n", chunk_size=200, chunk_overlap=0)
        chunks = splitter.split_documents(texts)
        
        print(f"Ingesting {len(chunks)} document chunks into FAISS...")
        db = FAISS.from_documents(chunks, embeddings)
        db.save_local(DB_FAISS_PATH)
        print("✅ Data ingested and FAISS index created successfully!")
        
    return db