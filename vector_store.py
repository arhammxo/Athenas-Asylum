from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
import os

def create_vector_store(text_chunks):
    embeddings = OpenAIEmbeddings(api_key=os.getenv("OPENAI_API_KEY"))
    return FAISS.from_texts(texts=text_chunks, embedding=embeddings) 
