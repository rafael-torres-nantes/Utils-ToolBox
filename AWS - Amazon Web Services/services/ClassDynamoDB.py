import boto3
from datetime import datetime
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import BotoCoreError, ClientError

class DynamoDBClass: 
    def __init__(self, dynamodb_table_name):

        # Criação de nome da Dynamo Table
        self.dynamodb_table_name = dynamodb_table_name

        # Inicia a sessão do DynamoDB
        self.dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

        # Inicia o serviço DynamoDB
        self.dynamodb_client = boto3.client('dynamodb', region_name='us-east-1')
    
    
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

            except (BotoCoreError, ClientError) as e: # Caso ocorra um erro, imprime a mensagem de erro
                print(f'Error: {e}')

        else:
            print('LOG: Tabela de log foi criada previamente.')            



    # Serviço de DynamoDB de cadastro de log
    def log_register_dynamodb(self, unique_id, phrase, s3_url):
            """
            Registra um log no DynamoDB contendo informações da requisição e resposta.

            :param request: Dados da requisição
            :return: None
            """
            # Inicia o serviço de DynamoDB e acessa a tabela especificada
            table = self.dynamodb.Table(self.dynamodb_table_name)  

            # Configura os dados do log
            log_item = {
                'id': unique_id,
                'timestamp': datetime.utcnow().isoformat(),
                'phrase': phrase,
                'url_to_audio': s3_url,
                'created_audio': datetime.utcnow().isoformat()
            }
                
            
            try: # Insere os dados do log na tabela do DynamoDB
                table.put_item(Item=log_item)
                print("Dados do log inseridos no DynamoDB com sucesso")
            
            except ClientError as e: # Caso ocorra um erro, imprime a mensagem de erro
                print(f"Erro ao inserir os dados do log no DynamoDB: {e}")

    def repeated_phrase_dynamodb(self, phrase):
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

            # Se houver itens, a frase foi encontrada
            if items:
                print(f"Frase '{phrase}' encontrada: {items}")
                return True
                
            # Se nenhum item for encontrado, a frase não foi encontrada
            else:
                print(f"Frase '{phrase}' não encontrada.")
                return False
        
        # Em caso de erro, imprime a mensagem de erro e retorna None
        except ClientError as e:
            print(f"Erro ao buscar a frase no DynamoDB: {e}")
            return None
    
    def repeated_value_dynamodb(self, unique_id):
        """
        Verifica se a frase já foi convertida

        :param unique_id: O unique_id a ser pesquisada no DynamoDB.
        :return: True se a frase for encontrada, False se não for encontrada, None em caso de erro.
        """
         # Inicializa o serviço DynamoDB e acessa a tabela especificada
        table = self.dynamodb.Table(self.dynamodb_table_name)
        
        
        try: # Usa a operação de get_item com um filtro para encontrar itens com a frase especificada
            response = table.get_item(Key={'id': unique_id}) # Obtém os itens retornados na resposta
            return 'Item' in response
        
        except ClientError as e: # Em caso de erro, imprime a mensagem de erro e retorna None
            print(f"Erro ao buscar a frase no DynamoDB: {e}")
            return None

    # Método para buscar o item no DynamoDB pelo ID
    def get_item(self, unique_id):
        table = self.dynamodb.Table(self.dynamodb_table_name)
        
        try: # Busca o item no DynamoDB pelo ID
            response = table.get_item(Key={'id': unique_id})
            return response.get('Item', {})
            
        except ClientError as e: # Caso ocorra um erro, retorna None
            print(f"Erro ao buscar o item no DynamoDB: {e}")
            return None
    
    def list_dynamodb_tables(self):
        try: # Lista as Tabelas do Dynamo
            response = self.dynamodb_client.list_tables()
            print("DynamoDB Tables:", response['TableNames'])
        
        except ClientError as e: # Caso ocorra um erro, retorna False
            print(f"Error listing DynamoDB tables: {e}")
            return False
        return True
