# Convert PDF chunks into FAISS index
import faiss
from sentence_transformers import SentenceTransformer
import numpy as np
import pickle
import os
from config import *
from pdf_utils import load_pdf_chunks

os.makedirs("index", exist_ok=True)
chunks = load_pdf_chunks(PDF_PATH)
model = SentenceTransformer(EMBED_MODEL_PATH)
embeddings = model.encode(chunks)

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))
faiss.write_index(index, INDEX_PATH)

with open("index/chunks.pkl", "wb") as f:
    pickle.dump(chunks, f)