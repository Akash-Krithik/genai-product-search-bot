from transformers import pipeline
from vectorstore import get_vectorstore

# Only load when actually needed
retriever = None
llm = None

def load_rag_pipeline():
    global retriever, llm
    if retriever is None:
        retriever = get_vectorstore().as_retriever()
    if llm is None:
        llm = pipeline("text2text-generation", model="google/flan-t5-base")

def get_answer(query):
    load_rag_pipeline()
    docs = retriever.invoke(query)
    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""You are a helpful assistant. Use the context below to answer the user's question.

Context:
{context}

Question: {query}
Answer:"""

    response = llm(prompt, max_length=256, do_sample=False)[0]['generated_text'].strip()
    return response, [doc.page_content for doc in docs]
