from dataclasses import dataclass, field
import numpy as np
@dataclass
class Chunk:
    """
    Represents a semantic chunk that grows as related sentences are added to it. Each chunk contains a list of sentences, their corresponding embeddings, and any associated metadata.
    
    """
    sentences: list[str]=field(default_factory=list)  #list of sentences in the chunk #default_factory=list is used to create a new empty list for each instance of the Chunk class, ensuring that each chunk has its own separate list of sentences
    embeddings: list[np.ndarray]=field(default_factory=list)  #list of embeddings for each sentence in the chunk
    metadata: dict = field(default_factory=dict)  #metadata for the chunk, such as source document, chunk id, etc.


    def add_sentence(self
                     , sentence:str,
                       embedding:np.ndarray
                       )-> None:
        """
        Adds a sentence and its corresponding embedding to the chunk.
        
        Args:
            sentence (str): The sentence to be added.
            embedding (np.ndarray): The embedding corresponding to the sentence.
        """
        self.sentences.append(sentence)  #append the sentence to the list of sentences
        self.embeddings.append(embedding)  #append the embedding to the list of embeddings

    @property
    def content(self) -> str:
        """
        Returns the concatenated content of all sentences in the chunk.
        
        Returns:
            str: The concatenated content of the chunk.
        """
        return " ".join(self.sentences)  #return the concatenated content of all sentences in the chunk
    
    @property
    def centroid(self)->np.ndarray:
        """
        Computes and returns the centroid of the embeddings in the chunk.
        
        Returns:
            np.ndarray: The centroid of the embeddings.
        """
        if not self.embeddings:
            return np.array([])  #return an empty array if there are no embeddings
        return np.mean(self.embeddings, axis=0)  #compute and return the centroid of the embeddings