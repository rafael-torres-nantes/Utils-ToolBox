import os
import json
import requests
import pandas as pd
from dotenv import load_dotenv

def load_json_file(json_file_path):
    
    with open(json_file_path, 'r') as file:
        json_data = json.load(file)

    return json_data

def main():
    # Dados para enviar no POST request
    data = load_json_file('./test_example.json')

    # Enviar o POST request
    response = requests.post("https://fbpdfs3097.execute-api.us-east-1.amazonaws.com/v1/vision", json=data)

    # Verificar se a request foi bem-sucedida
    if response.status_code == 200:
        result = response.json()
        print(result)
        
    else:
        print("Falha na predição. Status code:", response.status_code)
        print("Detalhes:", response.text)


if (__name__ == '__main__'):
    main()
