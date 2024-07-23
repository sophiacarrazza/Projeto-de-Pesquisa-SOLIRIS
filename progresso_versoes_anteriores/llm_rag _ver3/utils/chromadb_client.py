# Funções para interagir com o ChromaDB.
import sys
import os
import uuid
sys.path.append(os.path.abspath(os.path.join(os.path.dirname('utils/groq_client.py'), '..')))


import chromadb
from chromadb.utils import embedding_functions
from pdf_handling.extractor import extract_text_from_pdf

CHROMA_DATA_PATH = "chroma_data/"
EMBED_MODEL = "all-MiniLM-L6-v2"
COLLECTION_NAME = "ruth_docs"

client = chromadb.PersistentClient(path=CHROMA_DATA_PATH)

embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name=EMBED_MODEL
)
# Verifica se a coleção já existe, caso contrário, cria a coleção
collection_names = [collection.name for collection in client.list_collections()]
if COLLECTION_NAME not in collection_names:
    collection = client.create_collection(
        name=COLLECTION_NAME,
        embedding_function=embedding_func,
        metadata={"hnsw:space": "cosine"},
    )
else:
    collection = client.get_collection(name=COLLECTION_NAME)

def generate_id():
    return str(uuid.uuid4())

# Função para adicionar documentos à coleção
def add_text_to_collection(text, categories):
    # Dividindo o texto em documentos menores, se necessário
    documents = text.split("\n\n")  # Supondo que os parágrafos sejam separados por duas quebras de linha
    metadatas = [{"category": categories[i % len(categories)]} for i in range(len(documents))]
    ids = [generate_id() for _ in documents] # Gera um ID único para cada documento
    collection.add(documents=documents, metadatas=metadatas, ids=ids)

# Adiciona texto extraído de um PDF à coleção
pdf_path = "entrevistas.pdf"
categories = [
    "general",
    "technical_skills",
    "project_experience",
    "time_management",
    "teamwork",
    "career_choice",
    "marketing_campaign",
    "campaign_success",
    "marketing_tools",
    "handling_feedback",
]

text = extract_text_from_pdf()
add_text_to_collection(text, categories)

# Função para fazer consultas à coleção
def query_documents(query):
    query_vector = embedding_func.encode(query)
    results = collection.query(query_vectors=[query_vector], n_results=3)
    return results

# Exemplo de consulta
#query = "Gosto muito de utilizar Power BI!"
#results = query_documents(query)
#for result in results:
#    print(result)