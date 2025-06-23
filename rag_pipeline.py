from transformers import pipeline
from vectorstore import get_vectorstore

# Load retriever and model
retriever = get_vectorstore().as_retriever()
llm = pipeline("text2text-generation", model="google/flan-t5-base")

def get_answer(query):
    # Get relevant documents
    docs = retriever.get_relevant_documents(query)
    context = "\n".join([doc.page_content for doc in docs])

    # Construct flexible, dynamic prompt
    prompt = f"""You are a helpful assistant. Use the context below to answer the user's question.

Context:
{context}

Question: {query}
Answer:"""

    # Run the model
    response = llm(prompt, max_length=256, do_sample=False)[0]['generated_text'].strip()
    return response, [doc.page_content for doc in docs]
