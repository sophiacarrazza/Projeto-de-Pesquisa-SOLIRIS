# Funções para interagir com o Qdrant.

from qdrant_client import models, QdrantClient
#from qdrant_client.http.models import SearchRequest
from sentence_transformers import SentenceTransformer

# class QdrantClientWrapper:
#     def __init__(self, url):
#         self.client = QdrantClient(url)

#     def search(self, query_vector):
#         # Lógica para buscar informações relevantes no Qdrant
#         response = self.client.search(
#             collection_name='groq_ruth',
#             search_request=SearchRequest(
#                 vector=query_vector.tolist(),  # Converte o numpy array para uma lista
#                 limit=5
#             )
#         )
#         return response

encoder = SentenceTransformer("all-MiniLM-L6-v2")

#dataset 
doc_entrevistas = [
    {
        "name": "Entrevista de Emprego - TI",
        "description": "Conjunto de perguntas e respostas comuns em entrevistas de emprego na área de TI.",
        "category": "Entrevista de Emprego",
        "language": "Português",
        "questions_answers": [
            {
                "question": "Pode me falar um pouco sobre você?",
                "answer": "Eu sou formado em Ciência da Computação pela Universidade X e tenho 5 anos de experiência em desenvolvimento de software. Nos últimos anos, trabalhei principalmente com desenvolvimento web utilizando tecnologias como JavaScript, React e Node.js."
            },
            {
                "question": "Quais são suas principais habilidades técnicas?",
                "answer": "Minhas principais habilidades técnicas incluem programação em Java, Python e JavaScript, desenvolvimento de aplicações web com React e Node.js, e experiência com bancos de dados SQL e NoSQL. Também tenho conhecimento em metodologias ágeis como Scrum."
            },
            {
                "question": "Pode descrever um projeto recente em que você trabalhou?",
                "answer": "Recentemente, trabalhei em um projeto de e-commerce onde desenvolvemos uma plataforma para vendas online. Minha responsabilidade principal foi criar a interface de usuário usando React e integrar com a API backend desenvolvida em Node.js."
            },
            {
                "question": "Como você lida com prazos apertados?",
                "answer": "Quando enfrento prazos apertados, gosto de priorizar as tarefas mais importantes e dividir o trabalho em pequenas etapas gerenciáveis. Também mantenho uma comunicação constante com a equipe para garantir que todos estejam cientes do progresso e de quaisquer desafios que possam surgir."
            },
            {
                "question": "Qual é a sua experiência com trabalho em equipe?",
                "answer": "Tenho bastante experiência trabalhando em equipe. Em meus projetos anteriores, trabalhei em equipes multidisciplinares onde a colaboração e a comunicação eram essenciais para o sucesso do projeto. Valorizo muito o trabalho em equipe e acredito que a diversidade de perspectivas pode levar a soluções mais inovadoras."
            }
        ]
    },
    {
        "name": "Entrevista de Emprego - Marketing",
        "description": "Conjunto de perguntas e respostas comuns em entrevistas de emprego na área de Marketing.",
        "category": "Entrevista de Emprego",
        "language": "Português",
        "questions_answers": [
            {
                "question": "Por que você escolheu uma carreira em Marketing?",
                "answer": "Escolhi uma carreira em Marketing porque sempre fui fascinado por entender o comportamento do consumidor e por desenvolver estratégias criativas para promover produtos e serviços. Marketing combina análise de dados com criatividade, o que me permite usar diferentes habilidades."
            },
            {
                "question": "Pode descrever uma campanha de marketing bem-sucedida que você liderou?",
                "answer": "Liderei uma campanha de marketing digital para uma startup de tecnologia que resultou em um aumento de 30% nas vendas. A campanha utilizou uma combinação de anúncios pagos em redes sociais, email marketing segmentado e otimização de SEO para aumentar a visibilidade e o engajamento."
            },
            {
                "question": "Como você mede o sucesso de uma campanha de marketing?",
                "answer": "O sucesso de uma campanha de marketing pode ser medido através de diferentes KPIs (Key Performance Indicators), como aumento de vendas, taxa de conversão, ROI (Retorno sobre Investimento), engajamento em redes sociais e tráfego no site. É importante definir esses KPIs no início da campanha para avaliar seu desempenho de forma eficaz."
            },
            {
                "question": "Quais ferramentas de marketing você utiliza regularmente?",
                "answer": "Regularmente utilizo ferramentas como Google Analytics para análise de dados, SEMrush para SEO, Hootsuite para gerenciamento de redes sociais e Mailchimp para campanhas de email marketing. Essas ferramentas me ajudam a monitorar e ajustar as estratégias de marketing em tempo real."
            },
            {
                "question": "Como você lida com feedback negativo de uma campanha?",
                "answer": "Feedback negativo é uma oportunidade para melhorar. Primeiro, analiso o feedback para entender as preocupações dos clientes. Em seguida, faço ajustes na campanha e comunico as mudanças à equipe. Também é importante responder aos clientes para mostrar que estamos ouvindo e trabalhando para resolver os problemas."
            }
        ]
    }
]

client = QdrantClient(":memory:")

client.recreate_collection(
    collection_name="entrevista",
    vectors_config=models.VectorParams(
        size=encoder.get_sentence_embedding_dimension(),  # Vector size is defined by used model
        distance=models.Distance.COSINE,
    ),
)

client.upload_points(
    collection_name="entrevista",
    points=[
        models.PointStruct(
            id=idx, vector=encoder.encode(doc["description"]).tolist(), payload=doc
        )
        for idx, doc in enumerate(doc_entrevistas)
    ],
)

hits = client.search(
    collection_name="entrevista",
    query_vector=encoder.encode("amo marketing").tolist(),
    limit=3,
)
for hit in hits:
    print(hit.payload, "score:", hit.score)