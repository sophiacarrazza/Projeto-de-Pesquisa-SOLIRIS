# chatbot/rag.py

from utils.qdrant_client import QdrantClientWrapper
from transformers import AutoTokenizer, AutoModel

class RAGRetriever:
    def __init__(self, qdrant_url):
        self.qdrant_client = QdrantClientWrapper(qdrant_url)
        self.tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
        self.model = AutoModel.from_pretrained('bert-base-uncased')

    def embed_text(self, text):
        inputs = self.tokenizer(text, return_tensors='pt')
        outputs = self.model(**inputs)
        embeddings = outputs.last_hidden_state.mean(dim=1).squeeze().detach().numpy()
        return embeddings

    def retrieve(self, query):
        query_vector = self.embed_text(query)
        results = self.qdrant_client.search(query_vector)
        return results