#from chatterbot import ChatBot #importando o chatbot
#from chatterbot.trainers import ChatterBotCorpusTrainer

#chatbot = ChatBot( #criando o chatbot (o read_only=True é para que ele aprenda só com o treinamento, e nao com as conversas/com o usuario)
#    'Ruth',
#    read_only=True,
#    preprocessors=['chatterbot.preprocessors.clean_whitespace'],
#    tagger_language='pt_core_news_sm'
#) 
#trainer = ChatterBotCorpusTrainer(chatbot) #criando o treinador do chatbot

#trainer.train(
    #utilização de dados padrão que a biblioteca nos disponibiliza (os dados estao em portugues) - essa linha pode ser removida para trabalhar com outro BD
#    'chatterbot.corpus.portuguese',
#    './data/general.yml',
    #diretorio/caminho onde estão os arquivos de treinamento
#)

#if __name__ == '__main__':
#    while True:
#        try:
#            user_input = input('Usuário: ') #recebendo a solicitação do usuário
#            bot_response = chatbot.get_response(user_input)

#            print('Chatbot:', bot_response) #imprimindo a resposta do chatbot
#        except (KeyboardInterrupt, EOFError, SystemExit): #o laco fecha quando o usuário inserir CTRL + C ou CTRL + D
#            break

from rasa.jupyter import chat
from rasa.cli import utils as cli_utils
from rasa import model

def train_and_run_bot():
    # Train the Rasa model
    cli_utils.print_success("Training Rasa model...")
    model.train(domain="domain.yml", config="config.yml", training_files="./data")
    
    # Load the trained model
    cli_utils.print_success("Loading trained Rasa model...")
    trained_model_path = model.get_latest_model("models")
    interpreter = model.get_interpreter(trained_model_path)

    # Run the chatbot
    cli_utils.print_success("Chatbot is ready. You can start chatting!")
    chat(model_path=trained_model_path)

if __name__ == "__main__":
    train_and_run_bot()