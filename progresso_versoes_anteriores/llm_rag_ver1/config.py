# Arquivo para configuração de parâmetros, como caminhos de arquivos,
# configurações de banco de dados, etc.

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv('./.env')

# Definição das configurações
CONFIG = {
    'model_name': 'gpt-3.5-turbo',
    'api_key': '-',
    'qdrant_url': os.getenv('QDRANT_URL'),
    'GROQ_API_KEY': os.getenv('GROQ_API_KEY'),
    'chat': ChatGroq(temperature=0, model_name="mixtral-8x7b-32768", groq_api_key="-")
}