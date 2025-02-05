import base64

def encode_pdf_to_base64(file_path='./tmp/teste.pdf'):
    """
    Lê um arquivo PDF e converte para base64. 

    Args:
        file_path (str, optional): Caminho do arquivo PDF. Defaults to './tmp/teste.pdf'.
    Returns:
        bytes: Arquivo PDF convertido para base64 em bytes
    """
    # Lê o arquivo PDF e converte para base64
    with open(file_path, 'rb') as file:
        # Converte PDF para base64
        document_base64 = base64.b64encode(file.read())
        
        # O base64 precisa ser bytes, não string
        if isinstance(document_base64, str):
            document_base64 = document_base64.encode('utf-8')

    return document_base64

def decode_base64_to_pdf(document_base64, file_path='./tmp/decoded_test.pdf'):
    """
    Decodifica um arquivo PDF em base64 para um arquivo PDF.

    Args:
        document_base64 (bytes): Arquivo PDF convertido para base64 em bytes
        file_path (str, optional): Caminho do arquivo PDF decodificado. Defaults to './tmp/decoded_test.pdf'.
    """
    # Debug: Salva os bytes decodificados em um arquivo para verificar a integridade
    decoded_bytes = base64.b64decode(document_base64)
    with open(file_path, 'wb') as decoded_file:
        decoded_file.write(decoded_bytes)
    print('[DEBUG] Decoded document saved to ./tmp/decoded_test.pdf')
