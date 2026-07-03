from pathlib import Path 
from .document import Document

class TXTLoader:

    def load(self, path: str) -> Document:
        with open(path, 'r', encoding='utf-8') as file:
            text = file.read()

            return Document(
                source=path,
                content=text,
                metadata={
                    "type": "text",
                    "lines": len(text.splitlines())
                }
            )