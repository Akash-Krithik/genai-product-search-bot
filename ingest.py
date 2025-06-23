import pandas as pd
from langchain.schema import Document
from langchain.text_splitter import CharacterTextSplitter
from vectorstore import get_vectorstore

# Load CSV
df = pd.read_csv("data/electrical_products.csv")

# Combine rows into readable text
texts = []
for _, row in df.iterrows():
    content = f"Brand: {row['brand']}, Product: {row['product']}, Color: {row['color']}, Price: ₹{row['price']}, Offer: {row['offer_percent']}%"
    texts.append(Document(page_content=content))

# Split and store in ChromaDB
splitter = CharacterTextSplitter(separator="\n", chunk_size=200, chunk_overlap=0)
chunks = splitter.split_documents(texts)

db = get_vectorstore()
db.add_documents(chunks)

print("✅ Data ingested and vectorized!")
