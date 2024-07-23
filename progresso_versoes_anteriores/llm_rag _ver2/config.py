# Arquivo para configuração de parâmetros, como caminhos de arquivos,
# configurações de banco de dados, etc.

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from utils.chromadb_client import COLLECTION_NAME
from chatbot.rag import RAGRetriever

load_dotenv('./.env')

# Definição das configurações
CONFIG = {
    'chat': ChatGroq(temperature=0, model_name="mixtral-8x7b-32768", groq_api_key="-"),
    'rag_retriever': RAGRetriever(configchroma={'chromadb_collection': COLLECTION_NAME})
}