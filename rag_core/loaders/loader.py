from pathlib import Path

from .pdf_loader import PDFLoader
from .text_loader import TXTLoader
from .docx_loader import DOCXLoader

class DocumentLoader:

    def load(self,path:str):
        extension = Path(path).suffix.lower()

        if extension == ".pdf":
            loader = PDFLoader()
        elif extension == ".txt":
            loader = TXTLoader()
        elif extension == ".docx":
            loader = DOCXLoader()
        else:
            raise ValueError(f"Unsupported file type: {extension}")

        return loader.load(path)