# chatbot/rag.py
from utils.chromadb_client import query_documents


class RAGRetriever:
    def __init__(self, configchroma):
        self.collection = configchroma['chromadb_collection']

    def retrieve(self, query):
        return query_documents(query, self.collection)

#pergunta pro groq e o groq te da a resposta
# implementar o chatbot/chatbot.py aqui

#funcao principal que chama as demais