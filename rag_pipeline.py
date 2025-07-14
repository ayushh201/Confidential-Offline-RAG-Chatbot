import faiss
import numpy as np
import pickle
from sentence_transformers import SentenceTransformer
from llm_utils import ask_llm
from config import *

model = SentenceTransformer(EMBED_MODEL_PATH)
index = faiss.read_index(INDEX_PATH)

with open("index/chunks.pkl", "rb") as f:
    chunks = pickle.load(f)

def query_rag(question, top_k=3):
    q_emb = model.encode([question])
    D, I = index.search(np.array(q_emb), top_k)
    context = "\n".join([chunks[i] for i in I[0]])
    prompt = f"Answer based on context:\n{context}\n\nQ: {question}\nA:"
    return ask_llm(prompt), context