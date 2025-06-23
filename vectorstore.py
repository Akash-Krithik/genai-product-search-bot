# vectorstore.py

import os
import pandas as pd
# UPDATED: Import Document from langchain_core
from langchain_core.documents import Document
# UPDATED: Import CharacterTextSplitter from its new package
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

# Define the path for the persistent Chroma database
DB_DIR = "db"
DATA_PATH = "data/electrical_products.csv"

def get_vectorstore():
    """
    Initializes and returns a Chroma vector store.
    If the database doesn't exist on disk, it creates it by ingesting
    data from the specified CSV file.
    """
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    # Check if the database directory already exists and has been populated
    if os.path.exists(DB_DIR) and os.listdir(DB_DIR):
        print("✅ Database found on disk. Loading...")
    else:
        print("ℹ️ Database not found. Creating and ingesting data now...")
        
        # --- This is the ingestion logic from your ingest.py ---
        
        # 1. Load data from the CSV file
        df = pd.read_csv(DATA_PATH)
        
        # 2. Create Document objects for LangChain
        texts = []
        for _, row in df.iterrows():
            content = f"Brand: {row['brand']}, Product: {row['product']}, Color: {row['color']}, Price: ₹{row['price']}, Offer: {row['offer_percent']}%"
            texts.append(Document(page_content=content))

        # 3. Split the documents into smaller chunks
        splitter = CharacterTextSplitter(separator="\n", chunk_size=200, chunk_overlap=0)
        chunks = splitter.split_documents(texts)
        
        # 4. Create the Chroma database from the chunks and persist it
        print(f"Ingesting {len(chunks)} document chunks...")
        Chroma.from_documents(
            chunks, 
            embeddings, 
            persist_directory=DB_DIR
        )
        print("✅ Data ingested and database created successfully!")

    # Load the vector store from the persistent directory
    return Chroma(persist_directory=DB_DIR, embedding_function=embeddings)