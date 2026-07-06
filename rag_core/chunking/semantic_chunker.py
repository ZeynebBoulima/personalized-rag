# import re #used to split the text into sentences
# from sentence_transformers import SentenceTransformer  #Sentence transforms for lading an embedding model to convert sentences to vectors 
# from sentence_transformers.util import cos_sim #to compute the similarity between two sentences
# from rag_core.chunking.chunk import Chunk #our own chunk class to store the content and metadata of each chunk
# from rag_core.loaders.document import Document  #our own document class to store the content and metadata of each document
# import numpy as np  #used for numerical operations, especially for handling embeddings and calculating similarities
# class SemanticChunker:
#     def __init__(
#             self,
#             model_name: str = "all-MiniLM-L6-v2",  #default model name for the sentence transformer
#             similarity_threshold: float = 0.65,  #default similarity threshold for merging chunks
#     ):
#         self.model= SentenceTransformer(model_name)  #this loads the neural network model for sentence embeddings using the specified model name
#         self.similarity_threshold= similarity_threshold  #set the similarity threshold for merging chunks
        
# #sentence splitting is important for semantic chunking because it allows us to break down a large text into smaller, more manageable pieces. By splitting the text into sentences, we can analyze the meaning of each sentence individually and then group similar sentences together based on their semantic similarity. This helps in creating meaningful chunks of text that can be used for various natural language processing tasks, such as information retrieval, summarization, and question answering.

#     def split_into_sentences(self,text:str)-> list[str]:  #this method takes a string of text and returns a list of sentences
#         #split the text into sentences using regex
#         text=text.strip().replace("\n"," ")  #remove any leading/trailing whitespace and replace newlines with spaces
#         sentences = re.split(r'(?<=[.!?]) +', text)  #this regex splits the text at punctuation marks followed by a space
#         return [s.strip() for s in sentences if s.strip()]  #return the list of sentences
    
# #     input

# # AI is amazing.
# # Machine learning is useful.
# # Python is great.

# #    Output

# # [
# #     "AI is amazing.",
# #     "Machine learning is useful.",
# #     "Python is great."

# # ]
#     def encode_sentences(self,sentences:list[str])-> list[list[float]]:  #this method takes a list of sentences and returns a list of sentence embeddings
#         embeddings = self.model.encode(sentences)  #this uses the sentence transformer model to encode the sentences into embeddings
#         return embeddings  #return the list of embeddings


# #step 2 semantic similarity + chunk boundaries to determine which sentences should be grouped together into chunks. This is done by calculating the cosine similarity between the embeddings of each sentence and comparing it to a predefined threshold. If the similarity is above the threshold, the sentences are considered semantically similar and can be grouped together into a chunk.


#     def compute_similarities(self,embeddings):
#         similarities = []
#         for i in range(len(embeddings)-1):
#             sim=cos_sim(
#                 embeddings[i], embeddings[i+1]
#             ).item()  #compute the cosine similarity between the embeddings of two consecutive sentences
#             similarities.append(sim)  #append the similarity score to the list
#         return similarities  #return the list of similarity scores
    
#     def detect_boundaries(self, similarities):
#         boundaries = []

#         for i, sim in enumerate(similarities):
#             if sim < self.similarity_threshold:
#                 boundaries.append(i + 1)

#         return boundaries
    

#     def build_chunks(self, sentences, boundaries):
#         chunks = []
#         start = 0

#         for boundary in boundaries:
#             chunk_text = " ".join(sentences[start:boundary])

#             chunks.append(chunk_text)
#             start = boundary

#         # last chunk
#         chunk_text = " ".join(sentences[start:])
#         chunks.append(chunk_text)

#         return chunks
    
#     def chunk(self, text: str):
#         sentences = self.split_into_sentences(text)

#         embeddings = self.encode_sentences(sentences)

#         similarities = self.compute_similarities(embeddings)

#         boundaries = self.detect_boundaries(similarities)

#         chunks = self.build_chunks(sentences, boundaries)

#         return chunks


import numpy as np
from sentence_transformers import SentenceTransformer
from rag_core.chunking.chunk import Chunk

class SemanticChunker:
    def __init__(self,model_name="all-MiniLM-L6-v2",similarity_threshold=0.55):
        self.model = SentenceTransformer(model_name)
        self.similarity_threshold = similarity_threshold

    def split_into_sentences(self,text:str):
        import re
        text=text.strip().replace("\n"," ")
        sentences= re.split(r'(?<=[.!?]) +', text)
        return [s.strip() for s in sentences if s.strip()]
    
    def encode_sentences(self,sentences):
        return self.model.encode(sentences)
    
    def similarity(self,vec1,vec2):
        #cosine similarity between two vectors
        return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2)) #this calculates the cosine similarity between two vectors by taking the dot product of the vectors and dividing it by the product of their magnitudes (norms). The result is a value between -1 and 1, where 1 indicates that the vectors are identical, 0 indicates that they are orthogonal (unrelated), and -1 indicates that they are diametrically opposed.
    
    def chunk(self,text:str):
        sentences=self.split_into_sentences(text)
        embeddings=self.encode_sentences(sentences)
        chunks=[]
        current_chunk=Chunk()
        for sentence,embedding in zip(sentences,embeddings):
            if len(current_chunk.sentences)==0:
                current_chunk.add_sentence(sentence,embedding)
                continue
            sim=self.similarity(current_chunk.centroid,embedding)
            if sim>=self.similarity_threshold:
                current_chunk.add_sentence(sentence,embedding)

            else:
                chunks.append(current_chunk)
                current_chunk=Chunk()
                current_chunk.add_sentence(sentence,embedding)
        if current_chunk.sentences:
            chunks.append(current_chunk)

        return chunks