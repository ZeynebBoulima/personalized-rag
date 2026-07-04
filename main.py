from rag_core.loaders.loader import DocumentLoader

loader = DocumentLoader()

docs = loader.load("documents/django.txt")

print(docs.source)
print(docs.content[:200])


from rag_core.chunking.semantic_chunker import SemanticChunker

text = """
Artificial Intelligence is changing the world.
Machine learning is one branch of AI.
Deep learning uses neural networks.

Python is a programming language.
Functions help organize code.
"""

chunker = SemanticChunker(similarity_threshold=0.7)

chunks = chunker.chunk(text)

for i, chunk in enumerate(chunks):
    print(f"\nChunk {i+1}:\n{chunk}")