import streamlit as st
import pandas as pd
import os
from rag_pipeline import get_answer

st.set_page_config(page_title="Gen AI Product Search", layout="wide")
st.title("📦 Gen AI Product Search Bot")

# Dynamically load CSV from data folder
DATA_DIR = "data"
csv_files = [f for f in os.listdir(DATA_DIR) if f.endswith(".csv")]
if not csv_files:
    st.error("❌ No CSV files found in the data folder.")
    st.stop()

data_path = os.path.join(DATA_DIR, csv_files[0])
df = pd.read_csv(data_path)

# Define simple keyword categories
data_keywords = ["show", "data", "excel", "sheet", "table", "all products", "full data"]
greeting_keywords = ["hi", "hello", "hey", "how are you", "good morning", "good evening", "who are you", "your name"]
product_keywords = ["product", "price", "brand", "offer", "discount", "cost", "color", "buy", "rate"]

# Input box
query = st.text_input(
    "Ask a product-related question:",
    placeholder="e.g., Most discounted product name"
)

if st.button("Get Answer") and query:
    lower_query = query.lower()

    # 1. Redirect if it's just a greeting or unrelated small talk
    if any(greet in lower_query for greet in greeting_keywords) and not any(word in lower_query for word in product_keywords + data_keywords):
        st.warning("🙏 I'm here to help with product-related questions. Try asking something like: ‘Best offer on mixer’ or ‘Show product data’.")
    
    # 2. If user asked for full data
    elif any(word in lower_query for word in data_keywords):
        st.subheader("📊 Showing Top 10 Rows from Product Data")
        st.dataframe(df.head(10))
        st.info("⚠️ Data is large. Showing only top 10 rows. Download full data below.")
        
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Full Product Data (CSV)",
            data=csv,
            file_name=csv_files[0],
            mime="text/csv"
        )

    # 3. If it's a valid product-related query
    else:
        answer, sources = get_answer(query)
        st.subheader("🧠 Answer:")
        st.write(answer)
        st.subheader("📚 Sources:")
        for s in sources:
            st.code(s)
