import boto3
from datetime import datetime
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import BotoCoreError, ClientError
from services.importAWSCredentials import aws_credentials
from uuid import uuid4

class DynamoDBClass: 
    def __init__(self, dynamodb_table_name):
        # Cria uma viaravel global Dynamodb table name
        self.dynamodb_table_name = dynamodb_table_name

        # Importa as Credenciais da AWS
        self.session = self.create_session()

        # Inicia a sessão do DynamoDB
        self.dynamodb = self.session.resource('dynamodb', region_name='us-east-1')

        # Inicia o serviço DynamoDB
        self.dynamodb_client = self.session.client('dynamodb', region_name='us-east-1')


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
    
    def create_table_dynamodb(self):
        """
        Cria uma tabela no DynamoDB se ela ainda não existir.

        :return: None
        """
        # Lista as tabelas existentes no DynamoDB
        tables = self.dynamodb_client.list_tables()

        # Verifica se a tabela já existe
        if self.dynamodb_table_name not in tables['TableNames']:
            try:
                # Define o esquema da tabela e suas propriedades
                table = self.dynamodb.create_table(
                    TableName=self.dynamodb_table_name,
                    KeySchema=[
                        {
                            'AttributeName': 'id',
                            'KeyType': 'HASH'  # Define a chave primária da tabela
                        }
                    ],
                    AttributeDefinitions=[
                        {
                            'AttributeName': 'id',
                            'AttributeType': 'S'  # Define o tipo de atributo da chave primária como String
                        }
                    ],
                    ProvisionedThroughput={
                        'ReadCapacityUnits': 5,  # Define a capacidade de leitura provisionada
                        'WriteCapacityUnits': 5  # Define a capacidade de escrita provisionada
                    }
                )

                # Espera até que a tabela exista para confirmar a criação
                table.meta.client.get_waiter('table_exists').wait(TableName=self.dynamodb_table_name)

                print('LOG: Criação de Tabela de log concluída com sucesso.')

            except (BotoCoreError, ClientError) as e:
                print(f'Error: {e}')
        else:
            print('LOG: Tabela de log foi criada previamente.')            



    # Serviço de DynamoDB de cadastro de log
    def log_register_dynamodb(self, phrase):
            """
            Registra um log no DynamoDB contendo informações da requisição e resposta.

            :param request: Dados da requisição
            :return: None
            """
            # Inicia o serviço de DynamoDB e acessa a tabela especificada
            table = self.dynamodb.Table(self.dynamodb_table_name)        

            # Configura os dados do log
            log_item = {
                'id': str(uuid4()),  # Gera um ID único para o log
                'timestamp': datetime.utcnow().isoformat(),  # Obtém o timestamp atual no formato ISO
                'phrase': phrase,  # Dados da requisição
            }
                
            # Insere os dados do log na tabela do DynamoDB
            try:
                table.put_item(Item=log_item)
                print("Dados do log inseridos no DynamoDB com sucesso")
            except ClientError as e:
                print(f"Erro ao inserir os dados do log no DynamoDB: {e}")

    def repeated_value_dynamodb(self, phrase):
        """
        Verifica se há uma frase repetida no DynamoDB.

        :param phrase: A frase a ser pesquisada no DynamoDB.
        :return: True se a frase for encontrada, False se não for encontrada, None em caso de erro.
        """
        # Inicializa o serviço DynamoDB e acessa a tabela especificada
        table = self.dynamodb.Table(self.dynamodb_table_name)  

        # Usa a operação de scan com um filtro para encontrar itens com a frase especificada
        try:
            response = table.scan(
                FilterExpression=Attr('phrase').eq(phrase)
            )
            items = response.get('Items', [])  # Obtém os itens retornados na resposta
            if items:
                # Se houver itens, a frase foi encontrada
                print(f"Frase '{phrase}' encontrada: {items}")
                return True
            else:
                # Se nenhum item for encontrado, a frase não foi encontrada
                print(f"Frase '{phrase}' não encontrada.")
                return False
            
        except ClientError as e:
            # Em caso de erro, imprime a mensagem de erro e retorna None
            print(f"Erro ao buscar a frase no DynamoDB: {e}")
            return None

    
