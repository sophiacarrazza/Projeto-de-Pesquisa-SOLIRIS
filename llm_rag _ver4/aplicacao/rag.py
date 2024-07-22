import os
from langchain_core.prompts import PromptTemplate 
from langchain_groq import ChatGroq
from langchain.chains import create_retrieval_chain
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.vectorstores import Chroma
import PyPDF2
from langchain.text_splitter import RecursiveCharacterTextSplitter
import warnings

# Suppress specific FutureWarning from huggingface_hub
warnings.filterwarnings("ignore", message="`resume_download` is deprecated and will be removed in version 1.0.0")

# Caminho para o arquivo PDF
PDF_PATH = 'pdf_handling/entrevista_de_TI.pdf'

# Caminho para salvar os dados do ChromaDB
CHROMA_DATA_PATH = "chroma_data/"

# Modelo de embeddings
EMBED_MODEL = "all-MiniLM-L6-v2"

# Nome da coleção
COLLECTION_NAME = "ruth_docs"

# Função para extrair texto de um PDF e retornar uma lista de objetos Document
def extract_text_from_pdf(file_path):
    try:
        with open(file_path, 'rb') as pdf_file:
            pdf = PyPDF2.PdfReader(pdf_file)
            paginas = len(pdf.pages)
            text = ""
            for i in range(paginas):
                page = pdf.pages[i]
                text += page.extract_text()
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=500,
                chunk_overlap=50,
                length_function=len,
                separators=['\n','']
            )
            ftext = text.replace('\n', ' ')
            documents = text_splitter.create_documents([ftext])
            return documents
        
    except FileNotFoundError:
        print("Arquivo não encontrado")
        return []

class criar_vectordb:

    def save_db(self, documents, embeddings, db_path):
        self.db_path = db_path
        self.embeddings = embeddings
        self.documents = documents
        self._embedding_function= None
        vectordb = Chroma.from_documents(self.documents, self.embeddings, persist_directory=self.db_path, collection_name=COLLECTION_NAME)
        return vectordb
    
# embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2", model_kwargs={'device':'cpu'})
# hf_token = "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"


# Extraindo texto do PDF e criando a base de dados vetorial
documents = extract_text_from_pdf(PDF_PATH)
model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2", model_kwargs = {'device':'cpu'})
# model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
# documents_as_strings = [doc.page_content for doc in documents]
# embeddings = model.encode(documents_as_strings)

vectordb = criar_vectordb().save_db(documents, model, CHROMA_DATA_PATH)

os.environ["GROQ_API_KEY"] = "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"

ruth_prompt_template = """
                            Você é um assistente virtual de RH utilizando documentos para embasar suas respostas e perguntas sempre em fatos,
                            Use as informações presentes no documento para responder e fazer perguntas ao usuário candidato,
                            sua resposta deve ser o mais semelhante possível com a descrição presente nos documentos
                            
                            contexto: {context}
                            pergunta: {question}
                            
                            Apenas retorne as respostas úteis em ajudar na avaliação e seleção de candidatos relacionados ao documento e nada mais, com até uma linha de resposta, 
                            usando uma linguagem gentil e empática. Sempre responda em português, uma descrição em texto contínua, além disso adicione
                            um ou mais emojis às vezes para demonstrar empatia e emoção. 
                        
                            
                            
                            """

prompt = PromptTemplate(template=ruth_prompt_template, input_variables=['context', 'question'])
                            # Se o usuário responder de forma estranha ou não relacionada, você
                            # pode perguntar novamente ou pedir para ele reformular a pergunta. Além disso, se o usuário mencionar uma vaga que o nome não está 
                            # nos documentos, corrija o candidato mencionando a vaga correta. Além disso, se o usuário só digitar sim ou não, pergunte o motivo 
                            # e peça para ele explicar melhor. Pergunte ao candidato sobre suas experiências, habilidades e o que ele faria em determinadas situações
                            # e sobre o que ele ja passou em suas experiências.
'''
llm = CTransformers(
        model = "model/llama-2-7b-chat.ggmlv3.q8_0.bin",
        model_type = "llama",
        config={'max_new_tokens': 400, 
                'temperature': 0.2,
                'context_length': 10000,
                'repetition_penalty': 1.5,
                'top_p': 0.9,
                'top_k': 40
                }
        )
'''

llm = ChatGroq(model_name="llama3-70b-8192", api_key=os.environ["GROQ_API_KEY"])

retriever = vectordb.as_retriever(search_kwargs={"k": 2})
combine_docs_chain = create_stuff_documents_chain(
    llm, prompt
)

qa = create_retrieval_chain(retriever, combine_docs_chain)

# Main
#def main():
    # Exemplo de uso
#    context = "Feedback negativo"
#    question = "Como você lida com feedback negativo?"
#    response = qa.invoke({"context": context, "question": question}).get("answer")
#    print(response)

def mainRAG(question):
    # Exemplo de uso
    context = "Entrevista de emprego"
    response = qa.invoke({"context": context, "question": question}).get("answer")
    return response

# if __name__ == "__main__":
#    main()
