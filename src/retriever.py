from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

print("Loading Embedding Model...")

embedding_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

print("Embedding Model Loaded!")


class Retriever:

    def __init__(self):
        self.documents = []
        self.index = None

    def build_index(self, documents):

        self.documents = documents

        texts = [doc["content"] for doc in documents]

        embeddings = embedding_model.encode(
            texts,
            normalize_embeddings=True
        )

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatIP(dimension)

        self.index.add(np.array(embeddings).astype("float32"))

        print("FAISS Index Created Successfully!")

    def search(self, query, top_k=3):

        query_embedding = embedding_model.encode(
            [query],
            normalize_embeddings=True
        )

        distances, indices = self.index.search(
            np.array(query_embedding).astype("float32"),
            top_k
        )

        results = []

        for idx in indices[0]:
            results.append(self.documents[idx])

        return results