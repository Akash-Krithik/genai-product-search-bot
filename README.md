# 📦 Gen AI Product Search Bot

An AI-powered chatbot that helps users find answers about electrical products using natural language queries. Built using **LangChain**, **HuggingFace Transformers**, **ChromaDB**, and **Streamlit**.

---

## 🚀 Features

- 🧠 Question answering with context
- 🔍 Intelligent product search using vector embeddings
- ⚙️ LLM-based response generation (Google Flan-T5)
- 🧾 CSV-based product ingestion and storage
- 🌐 Simple web UI built with Streamlit

---

## 🧰 Tech Stack

| Layer        | Tool/Library                      |
|--------------|-----------------------------------|
| Interface    | Streamlit                         |
| Embeddings   | `all-MiniLM-L6-v2` via HuggingFace|
| Vector Store | ChromaDB                          |
| LLM          | `google/flan-t5-base`             |
| Framework    | LangChain                         |

---

## 🗂️ Folder Structure

GenAI-ProductSearchBot/
├── app.py # Streamlit frontend
├── ingest.py # CSV ingestion & vectorization
├── rag_pipeline.py # Retrieval + Generation pipeline
├── vectorstore.py # Vector DB logic
├── data/
│ └── electrical_products.csv # Sample product dataset
└── db/ # Vector DB directory (ignored in Git)

---

## ▶️ How to Run

1. **Install dependencies**  
   ```bash
   pip install -r requirements.txt

2. **Ingest product data**

python ingest.py

3.  **Run the app**

streamlit run app.py


 Sample Query
“Which fan has the highest discount?”
“Tell me about a white colored product under ₹2000”

Author
Akash Krithik
LinkedIn:- https://www.linkedin.com/in/akash-krithik-344486214/

