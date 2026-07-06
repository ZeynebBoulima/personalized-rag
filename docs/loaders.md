# Document Loading

## Purpose

The document loading module is responsible for reading documents from different file formats and converting them into a common internal representation.

The goal is to isolate all file-specific logic from the rest of the RAG pipeline.

---

## Architecture

Document
        ↑
PDF Loader
DOCX Loader
TXT Loader
        ↑
DocumentLoader (abstract base class)

---

## Why use a common Document model?

Every loader returns the same object regardless of the source format.

This allows downstream components (chunking, embeddings, retrieval) to process documents without knowing whether they originated from a PDF, a Word document, or a text file.

Without a common model, every component would require format-specific logic, increasing coupling and making the system harder to maintain.

---

## Why use an abstract base class?

The abstract `DocumentLoader` defines a common interface for every loader.

Each implementation must provide a `load()` method.

This follows the Open/Closed Principle:

- open for extension
- closed for modification

Adding support for a new file type only requires implementing another loader.

---

## Current supported formats

- TXT
- PDF
- DOCX

---

## Future improvements

- HTML loader
- Markdown loader
- OCR support
- Metadata extraction