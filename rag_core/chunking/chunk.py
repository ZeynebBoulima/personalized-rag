from dataclasses import dataclass

@dataclass
class chunk:
    content:str
    metadata:dict





# Exactly like the Document model.

# A chunk is simply another object with

# its text
# its metadata

# For example

# Chunk(
#     content="Machine learning is a subset of AI...",
#     metadata={
#         "source": "AI.pdf",
#         "chunk_id": 2
#     }
# )