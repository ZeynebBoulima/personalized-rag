from pathlib import Path #pathlib is python library that provides an object-oriented interface for working with file system paths. It allows you to manipulate and interact with file paths in a more intuitive way compared to traditional string-based methods.
from pypdf import PdfReader #the PdfReader class is part of the PyPDF2 library, which is a Python library for working with PDF files. It allows you to read and extract information from PDF documents, such as text, images, metadata, and more.
from .document import Document #this imports the document class that we created earlier in the document.py file. The Document class is a data structure that represents a document with its source, content, and metadata. 

class PDFLoader:

    def load(self,path:str) -> Document: #self refers to the current object
        pdf=PdfReader(path)

        text = ""

        for page in pdf.pages:
            extracted = page.extract_text()

            if extracted: #nekhou ken non-empty text
                text += extracted +"\n" #The "\n" adds a newline between pages to keep the text readable.

        return Document(
            source=path,
            content=text,
            metadata={
                "type": "pdf",
                "pages": len(pdf.pages)}
        )



   
