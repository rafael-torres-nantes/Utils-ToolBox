import os
import boto3
import logging
from dotenv import load_dotenv
from botocore.exceptions import ClientError
from services.importAWSCredentials import aws_credentials

class S3BucketClass: 
    def __init__(self, bucket_name):

        # Cria uma viaravel global bucket name
        self.bucket_name = bucket_name

        # Importa as Credenciais da AWS
        self.session = self.create_session()

        # Inicia o serviço S3 Bucket
        self.s3_client = self.session.client('s3')
         
    
    def create_session(self):
        """
        Cria uma sessão AWS utilizando as credenciais obtidas de aws_credentials.

        :return: Uma sessão boto3
        """
        # Obtem as chaves de acesso da AWS
        ACCESS_KEY, SECRET_KEY, SESSION_TOKEN = aws_credentials()

        # Conecta com AWS por meio das credenciais
        session = boto3.Session(
            aws_access_key_id=ACCESS_KEY, 
            aws_secret_access_key=SECRET_KEY,
            aws_session_token=SESSION_TOKEN
        )
        return session


    def create_s3_bucket(self):
        """
        Cria um bucket S3 com o nome especificado.

        :param bucket_name: Nome do bucket a ser criado
        :return: True se o bucket for criado com sucesso, caso contrário False
        """
        # Importa o bucket name da Classe
        bucket_name = self.bucket_name

        try:
            # Cria o bucket
            self.s3_client.create_bucket(Bucket=bucket_name)
            self.session.resource('s3').Bucket(bucket_name)
            
        except ClientError as e:
            logging.error(e)
            return False
        return True

    def list_s3_bucket(self):
        """
        Lista os nomes dos buckets S3 existentes.

        :return: Lista de nomes de buckets
        """
        # Recupera a lista de buckets existentes
        list_buckets = self.s3_client.list_buckets()

        # Exibe os nomes dos buckets
        for bucket in list_buckets['Buckets']:
            print(f'{bucket["Name"]}')

        return list_buckets['Buckets']

    def upload_s3_bucket(self, upload_file, filename):
        """
        Faz o upload de um arquivo para um bucket S3.

        :param bucket_name: Nome do bucket para onde o arquivo será enviado
        :param upload_file: Caminho do arquivo a ser enviado
        :param filename: Nome do objeto no S3. Se não especificado, o nome do arquivo será usado
        :return: True se o arquivo for enviado com sucesso, caso contrário False
        """
        try:
            # Faz o upload do arquivo
            self.s3_client.upload_file(upload_file, self.bucket_name, filename)

        # Upload a object(The upload_fileobj method accepts a readable file-like object. The file object must be opened in binary mode, not text mode.)
        # with open("FILE_NAME", "rb") as f:
        #     s3_client.upload_fileobj(f, bucket_name, "OBJECT_NAME")
        
        except ClientError as e:
            logging.error(e)
            return False

        return True
        

    def extract_file_s3_bucket(self, object_key):
        """
        Faz o download de um arquivo de um bucket S3.

        :param object_key: Caminho do arquivo no S3
        :return: Caminho do diretório local onde o arquivo foi baixado
        """

        # Importa o bucket name da Classe
        bucket_name = self.bucket_name

        # Diretório local para onde o arquivo será baixado
        local_directory = '../download'

        if not os.path.exists(local_directory):
            os.makedirs(local_directory)

        # Faz o download do arquivo do bucket S3
        self.s3_client.download_file(bucket_name, object_key, os.path.join(local_directory, object_key))

        return local_directory

load_dotenv()
S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME')

criar_classe = S3BucketClass(S3_BUCKET_NAME)
