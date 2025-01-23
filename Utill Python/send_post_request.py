import os
import json
import requests
import pandas as pd
from dotenv import load_dotenv

def load_json_file(json_path):
    """
    Função para carregar um arquivo JSON.

    Args:
        json_path (str): Caminho do arquivo JSON.
    """
    
    with open(json_path, 'r') as file:
        json_data = json.load(file)

    return json_data

def send_post_request():
    """
    Função para enviar um POST request para a API qualquer.

    Returns:
        dict: Resultado da API.
    """

    # Dados para enviar no POST request
    data = load_json_file('./test_example.json')

    # Enviar o POST request para a API
    response = requests.post("https://fbpdfs3097.execute-api.us-east-1.amazonaws.com/v1/vision", json=data)

    # Verificar se a request foi bem-sucedida
    if response.status_code == 200:
        result = response.json()
        print(result)
        
    else:
        print("Falha na predição. Status code:", response.status_code)
        print("Detalhes:", response.text)


if (__name__ == '__main__'):
    send_post_request()
