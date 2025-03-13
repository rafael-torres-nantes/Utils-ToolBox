import pandas as pd

def read_multiple_sheets_from_excel(file_path):
    """
    Função para ler múltiplos sheets de um arquivo Excel

    Args:
        file_path (str): Caminho do arquivo Excel

    Returns:
        dict: Dicionário com os dados
    """
    try:
        # Abre o arquivo Excel
        excel_file = pd.ExcelFile(file_path)
        
        # Obtém os nomes de todas as sheets
        sheet_names = excel_file.sheet_names
        
        file_data = {}
        
        # Processa cada sheet do arquivo
        for sheet_name in sheet_names:
            # Carrega a sheet para um DataFrame
            df = excel_file.parse(sheet_name)
            
            # Converte o DataFrame para um dicionário e armazena
            records = df.to_dict(orient='records')
            file_data[sheet_name] = records
        
        # Retorna o dicionário com os dados
        return file_data
    
    except Exception as e:
        # If an error occurs while processing the file, return an error message
        return {"Error": f"Erro ao processar o arquivo {file_path}: {e}"}
