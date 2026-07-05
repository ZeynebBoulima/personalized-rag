# Personalized RAG

A Retrieval-Augmented Generation (RAG) system built from scratch in Python.

## 🚀 Goals

- Build every RAG component manually
- Understand how each component works
- Avoid relying on LangChain for the core pipeline
- Produce production-quality, well-documented code

## 📂 Project Structure

```text
personalized-rag/
│
├── documents/
├── rag_core/
│   ├── chunking/
│   ├── embeddings/
│   ├── llm/
│   ├── loaders/
│   └── vectordb/
│
├── tests/
├── main.py
└── requirements.txt
```

## 🛠 Current Progress

- [x] Project setup
- [x] Document abstraction
- [x] TXT loader
- [x] PDF loader
- [x] DOCX loader
- [x] Initial semantic chunking
- [ ] Improved semantic chunking
- [ ] Embedding pipeline
- [ ] Vector database
- [ ] Retrieval
- [ ] Gemini integration

## 📜 License

MIT License