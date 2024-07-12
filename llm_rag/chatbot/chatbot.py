# Classe principal do chatbot.
from models.model import ChatBotModel
from langchain.schema import SystemMessage, HumanMessage, AIMessage
from chatbot.rag import RAGRetriever

class ChatBot:
    def __init__(self, config):
        self.model = ChatBotModel(config['model_name'], config['api_key'])
        self.rag = RAGRetriever(config['qdrant_url'])
        self.messages = [
            SystemMessage(content="You are a helpful assistant."),
            HumanMessage(content="Hi AI, how are you today?"),
            AIMessage(content="I'm great thank you. How can I help you?"),
            HumanMessage(content="I'd like to understand machine learning.")
        ]

    def start(self):
        while True:
            user_input = input("You: ")
            self.messages.append(HumanMessage(content=user_input))
            
            # Use o RAG para buscar informações relevantes
            retrieved_docs = self.rag.retrieve(user_input)
            context = "\n".join([doc['text'] for doc in retrieved_docs])
            
            # Adicione o contexto aos messages
            self.messages.append(SystemMessage(content=f"Relevant context: {context}"))
            
            response = self.model.get_response(self.messages)
            print(f"Bot: {response}")