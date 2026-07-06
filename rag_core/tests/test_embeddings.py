from sentence_transformers import SentenceTransformer   

model = SentenceTransformer("all-MiniLM-L6-V2")

embeddings = model.encode(
'Artificial Intelligence is changing the world.')

print(type(embeddings))
print(embeddings.shape)
print(embeddings[:10])