from rag_core.loaders.loader import DocumentLoader

loader = DocumentLoader()

docs = loader.load("documents/django.txt")

print(docs.source)
print(docs.content[:200])


from rag_core.chunking.semantic_chunker import SemanticChunker





import numpy as np

from rag_core.chunking.chunk import Chunk

chunk = Chunk()

chunk.add_sentence(
    "Artificial Intelligence is changing the world.",
    np.array([1.0, 2.0, 3.0])
)

chunk.add_sentence(
    "Machine learning is a branch of AI.",
    np.array([4.0, 5.0, 6.0])
)

print(chunk.content)
print(chunk.centroid)

# text = """
# Artificial Intelligence is changing the world.
# Machine learning is one branch of AI.
# Deep learning uses neural networks.

# Python is a programming language.
# Functions help organize code.
# """

# chunker = SemanticChunker(similarity_threshold=0.7)

# chunks = chunker.chunk(text)

# for i, chunk in enumerate(chunks):
#     print(f"\nChunk {i+1}:\n{chunk}")