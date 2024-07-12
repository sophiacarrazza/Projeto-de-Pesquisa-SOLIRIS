# Funções para interagir com o ChromaDB.

import chromadb
from chromadb.utils import embedding_functions

CHROMA_DATA_PATH = "chroma_data/"
EMBED_MODEL = "all-MiniLM-L6-v2"
COLLECTION_NAME = "ruth_docs"

client = chromadb.PersistentClient(path=CHROMA_DATA_PATH)

embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name=EMBED_MODEL
)

# Check if the collection 'ruth_docs' exists
#if 'ruth_docs' not in client.collections():
    # If the collection does not exist, create it
collection = client.create_collection(
    name=COLLECTION_NAME,
    embedding_function=embedding_func,
    metadata={"hnsw:space": "cosine"},
)

documents = [
    "Pode me falar um pouco sobre você?",
    "Quais são suas principais habilidades técnicas?",
    "Pode descrever um projeto recente em que você trabalhou?",
    "Como você lida com prazos apertados?",
    "Qual é a sua experiência com trabalho em equipe?",
    "Por que você escolheu uma carreira em Marketing?",
    "Pode descrever uma campanha de marketing bem-sucedida que você liderou?",
    "Como você mede o sucesso de uma campanha de marketing?",
    "Quais ferramentas de marketing você utiliza regularmente?",
    "Como você lida com feedback negativo de uma campanha?",
]

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

answers = [
    "Eu sou formado em Ciência da Computação pela Universidade X e tenho 5 anos de experiência em desenvolvimento de software. Nos últimos anos, trabalhei principalmente com desenvolvimento web utilizando tecnologias como JavaScript, React e Node.js.",
    "Minhas principais habilidades técnicas incluem programação em Java, Python e JavaScript, desenvolvimento de aplicações web com React e Node.js, e experiência com bancos de dados SQL e NoSQL. Também tenho conhecimento em metodologias ágeis como Scrum.",
    "Recentemente, trabalhei em um projeto de e-commerce onde desenvolvemos uma plataforma para vendas online. Minha responsabilidade principal foi criar a interface de usuário usando React e integrar com a API backend desenvolvida em Node.js.",
    "Quando enfrento prazos apertados, gosto de priorizar as tarefas mais importantes e dividir o trabalho em pequenas etapas gerenciáveis. Também mantenho uma comunicação constante com a equipe para garantir que todos estejam cientes do progresso e de quaisquer desafios que possam surgir.",
    "Tenho bastante experiência trabalhando em equipe. Em meus projetos anteriores, trabalhei em equipes multidisciplinares onde a colaboração e a comunicação eram essenciais para o sucesso do projeto. Valorizo muito o trabalho em equipe e acredito que a diversidade de perspectivas pode levar a soluções mais inovadoras.",
    "Escolhi uma carreira em Marketing porque sempre fui fascinado por entender o comportamento do consumidor e por desenvolver estratégias criativas para promover produtos e serviços. Marketing combina análise de dados com criatividade, o que me permite usar diferentes habilidades.",
    "Liderei uma campanha de marketing digital para uma startup de tecnologia que resultou em um aumento de 30% nas vendas. A campanha utilizou uma combinação de anúncios pagos em redes sociais, email marketing segmentado e otimização de SEO para aumentar a visibilidade e o engajamento.",
    "O sucesso de uma campanha de marketing pode ser medido através de diferentes KPIs (Key Performance Indicators), como aumento de vendas, taxa de conversão, ROI (Retorno sobre Investimento), engajamento em redes sociais e tráfego no site. É importante definir esses KPIs no início da campanha para avaliar seu desempenho de forma eficaz.",
    "Regularmente utilizo ferramentas como Google Analytics para análise de dados, SEMrush para SEO, Hootsuite para gerenciamento de redes sociais e Mailchimp para campanhas de email marketing. Essas ferramentas me ajudam a monitorar e ajustar as estratégias de marketing em tempo real.",
    "Feedback negativo é uma oportunidade para melhorar. Primeiro, analiso o feedback para entender as preocupações dos clientes. Em seguida, faço ajustes na campanha e comunico as mudanças à equipe. Também é importante responder aos clientes para mostrar que estamos ouvindo e trabalhando para resolver os problemas."
]

query_results = collection.query(
    query_texts=["Gosto muito de utilizar Power BI!"],
    n_results=1,
)

def query_documents(query):
    query_vector = embedding_func.encode(query)
    results = collection.query(query_vectors=[query_vector], n_results=3)
    return results  # List of Document objects
