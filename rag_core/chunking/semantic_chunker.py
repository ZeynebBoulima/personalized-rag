import re #used to split the text into sentences
from sentence_transformers import SentenceTransformer  #Sentence transforms for lading an embedding model to convert sentences to vectors 
from sentence_transformers.util import cos_sim #to compute the similarity between two sentences
from rag_core.chunking.chunk import Chunk #our own chunk class to store the content and metadata of each chunk
from rag_core.loaders.document import Document  #our own document class to store the content and metadata of each document
import numpy as np  #used for numerical operations, especially for handling embeddings and calculating similarities
class SemanticChunker:
    def __init__(
            self,
            model_name: str = "all-MiniLM-L6-v2",  #default model name for the sentence transformer
            similarity_threshold: float = 0.5,  #default similarity threshold for merging chunks
    ):
        self.model= SentenceTransformer(model_name)  #this loads the neural network model for sentence embeddings using the specified model name
        self.similarity_threshold= similarity_threshold  #set the similarity threshold for merging chunks
        
#sentence splitting is important for semantic chunking because it allows us to break down a large text into smaller, more manageable pieces. By splitting the text into sentences, we can analyze the meaning of each sentence individually and then group similar sentences together based on their semantic similarity. This helps in creating meaningful chunks of text that can be used for various natural language processing tasks, such as information retrieval, summarization, and question answering.

    def split_into_sentences(self,text:str)-> list[str]:  #this method takes a string of text and returns a list of sentences
        #split the text into sentences using regex
        text=text.strip().replace("\n"," ")  #remove any leading/trailing whitespace and replace newlines with spaces
        sentences = re.split(r'(?<=[.!?]) +', text)  #this regex splits the text at punctuation marks followed by a space
        return [s.strip() for s in sentences if s.strip()]  #return the list of sentences
    
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
    def encode_sentences(self,sentences:list[str])-> list[list[float]]:  #this method takes a list of sentences and returns a list of sentence embeddings
        embeddings = self.model.encode(sentences)  #this uses the sentence transformer model to encode the sentences into embeddings
        return embeddings  #return the list of embeddings


#step 2 semantic similarity + chunk boundaries to determine which sentences should be grouped together into chunks. This is done by calculating the cosine similarity between the embeddings of each sentence and comparing it to a predefined threshold. If the similarity is above the threshold, the sentences are considered semantically similar and can be grouped together into a chunk.


    def compute_similarities(self,embeddings):
        similarities = []
        for i in range(len(embeddings)-1):
            sim=cos_sim(
                embeddings[i], embeddings[i+1]
            ).item()  #compute the cosine similarity between the embeddings of two consecutive sentences
            similarities.append(sim)  #append the similarity score to the list
        return similarities  #return the list of similarity scores
    
    def detect_boundaries(self, similarities):
        boundaries = []

        for i, sim in enumerate(similarities):
            if sim < self.similarity_threshold:
                boundaries.append(i + 1)

        return boundaries
    

    def build_chunks(self, sentences, boundaries):
        chunks = []
        start = 0

        for boundary in boundaries:
            chunk_text = " ".join(sentences[start:boundary])

            chunks.append(chunk_text)
            start = boundary

        # last chunk
        chunk_text = " ".join(sentences[start:])
        chunks.append(chunk_text)

        return chunks
    
    def chunk(self, text: str):
        sentences = self.split_into_sentences(text)

        embeddings = self.encode_sentences(sentences)

        similarities = self.compute_similarities(embeddings)

        boundaries = self.detect_boundaries(similarities)

        chunks = self.build_chunks(sentences, boundaries)

        return chunks