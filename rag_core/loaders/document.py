from dataclasses import dataclass

@dataclass
class Document:
    source: str #name mtaa file mteei
    content: str #el content mtaa file mteei
    metadata: dict # bech nalka feha data kima page number, author, title, type etc