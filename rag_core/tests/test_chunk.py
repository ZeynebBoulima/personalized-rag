from rag_core.chunking.semantic_chunker import SemanticChunker

text = """
Artificial Intelligence is changing the world.
Machine learning is a branch of AI.
Deep learning uses neural networks.

Python is a programming language.
Functions help organize code.
"""

chunker = SemanticChunker(similarity_threshold=0.6)

chunks = chunker.chunk(text)

for i, c in enumerate(chunks):
    print(f"\nChunk {i+1}")
    print(c.content)