from rag_core.loaders.loader import DocumentLoader

loader = DocumentLoader()

docs = loader.load("documents/django.txt")

print(docs.source)
print(docs.content[:200])