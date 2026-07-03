import re #used to split the text into sentences
from sentence_transformers import SentenceTransformer  #Sentence transforms for lading an embedding model to convert sentences to vectors 
from sentence_transormers.util import cos_sim #to compute the similarity between two sentences
from rag_core.chunking.chunk import Chunk #our own chunk class to store the content and metadata of each chunk
from rag_core.loaders.loader import Document  #our own document class to store the content and metadata of each document


class SemanticChunker:
    def __init__(
            self,
            model_name: str = "all-MiniLM-L6-v2",  #default model name for the sentence transformer
            similarity_threshold: float = 0.75,  #default similarity threshold for merging chunks
    ):
        self.model= SentenceTransformer(model_name)  #this loads the neural network model for sentence embeddings using the specified model name
        self.similarity_threshold= similarity_threshold  #set the similarity threshold for merging chunks
        

    def split_into_sentences(self,text:str):
        #split the text into sentences using regex
        sentences = re.split(r'(?<=[.!?]) +', text)  #this regex splits the text at punctuation marks followed by a space
        return sentences  #return the list of sentences
    
#     input

# AI is amazing.
# Machine learning is useful.
# Python is great.

#    Output

# [
#     "AI is amazing.",
#     "Machine learning is useful.",
#     "Python is great."
# ]