from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')  # Small, fast, good accuracy
model.save('embeddings/embedding_model')
