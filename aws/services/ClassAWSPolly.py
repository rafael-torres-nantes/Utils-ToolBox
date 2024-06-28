import boto3
import os
import io
from pydub import AudioSegment
from pydub.playback import play
from dotenv import load_dotenv
from botocore.exceptions import BotoCoreError, ClientError
from services.importAWSCredentials import aws_credentials
import sys

class TTSClass: 
    def __init__(self):

        # Importa as Credenciais da AWS
        self.session = self.create_session()

        # Inicia o serviço Polly
        self.polly_client = self.session.client('polly')

        # Frase placeholder para ser trocada
        self.phrase = 'placeholder'

        # Seleciona a voz feminina Joanna
        self.voiceId = 'Joanna'

        # Formato de saída do áudio
        self.outputFormat = 'mp3'
    
    def create_session(self):
        """
        Cria uma sessão AWS utilizando as credenciais obtidas de aws_credentials.

        :return: Uma sessão boto3
        """
        # Obtém as chaves de acesso da AWS
        ACCESS_KEY, SECRET_KEY, SESSION_TOKEN = aws_credentials()

        # Conecta com AWS por meio das credenciais
        session = boto3.Session(
            aws_access_key_id=ACCESS_KEY, 
            aws_secret_access_key=SECRET_KEY,
            aws_session_token=SESSION_TOKEN
        )
        return session


    def textToSpeech(self, phrase):
        """
        Converte o texto fornecido em fala usando o serviço AWS Polly e retorna o áudio como bytes.

        :param phrase: Texto a ser convertido em fala
        :return: Os bytes do áudio sintetizado se a conversão for bem-sucedida, caso contrário None
        """
                
        # Armazena o texto do text to speech
        self.phrase = phrase

        # Tenta sintetizar a fala em áudio MP3 com a voz da AWS Polly e retorna o stream de áudio
        try:
            # Solicita a síntese de fala ao serviço Polly
            self.response = self.polly_client.synthesize_speech(
                Text=phrase,
                OutputFormat=self.outputFormat, # Formato de saída do áudio
                VoiceId = self.voiceId # Seleciona a voz feminina Joanna
            )
            # Obtém os bytes do áudio sintetizado a partir do stream de áudio na resposta
            return self.response['AudioStream'].read()  # Retorna os bytes do áudio
        
        # Captura e trata exceções de cliente (por exemplo, erros de permissão)
        except ClientError as e:
            # Imprime a mensagem de erro e retorna None
            print(e.response['Error']['Message'])
            return None
        

    def saveMP3File(self):
        """
        Reproduz o áudio sintetizado.

        :return: None
        """

        # Verifica se a resposta da solicitação de síntese de fala contém um stream de áudio
        if "AudioStream" in self.response:
            # Abre o stream de áudio como um arquivo temporário
            with self.response["AudioStream"] as stream:
                # Define o Diretório do arquivo de saída como "speech.mp3"
                local_directory = './audio_files'

                if not os.path.exists(local_directory):
                    os.makedirs(local_directory)
                    
                # Define o nome do arquivo de saída como "speech.mp3"
                self.output_file = f'{local_directory}/speech.mp3'
                try:
                    # Abre um arquivo para escrever os bytes do áudio como um arquivo MP3
                    with open(self.output_file, "wb") as file:
                        # Escreve os bytes do áudio no arquivo
                        file.write(stream.read())
                except IOError as error:
                    # Imprime o erro caso ocorra um problema ao escrever no arquivo
                    print(error)
        else:
            # Se a resposta não contiver um stream de áudio, imprime uma mensagem indicando que não foi possível transmitir o áudio
            print("Não foi possível transmitir o áudio")

    def playMP3File(self):
        # Reproduz o áudio usando o reprodutor padrão do sistema operacional
        if sys.platform == "win32":
            # Inicia a reprodução do arquivo de áudio no Windows
            os.startfile(self.output_file)


# Instância da classe TTSClass
criar_classe = TTSClass()

# Solicita a síntese de fala para a frase "bom dia"
criar_classe.textToSpeech('bom dia')

# Reproduz o áudio sintetizado
criar_classe.saveMP3File()
