# Como Alterar o Timeout de uma Função Lambda

Este guia fornece instruções detalhadas sobre como configurar o valor de timeout para uma função Lambda usando o console da AWS, a AWS CLI e o AWS Serverless Application Model (SAM).

## Introdução

O valor de timeout de uma função Lambda define o tempo máximo que a função pode ser executada antes de ser interrompida. A duração da execução pode variar com base na quantidade de dados transferidos, processamento necessário e latência de serviços externos. Configurar um timeout adequado ajuda a evitar falhas inesperadas.

## Configurar Timeout no Console da AWS

1. **Acesse o console da AWS**: [AWS Management Console](https://aws.amazon.com/console/)
2. **Navegue até o Lambda**:
   - No campo de busca, digite "Lambda" e clique no serviço Amazon Lambda.
3. **Escolha uma Função**:
   - Selecione a função Lambda que deseja configurar.
4. **Vá para Configuração Geral**:
   - Clique na aba "Configuration" e depois em "General configuration".
5. **Edite o Timeout**:
   - Clique em "Edit" na seção "General configuration".
   - Para "Timeout", defina um valor entre 1 e 900 segundos (15 minutos).
   - Clique em "Save" para salvar as mudanças.

![image](https://github.com/rafael-torres-nantes/Utils-ToolBox/assets/58231791/869004dc-b865-4c12-8874-b05555c40534)

## Configurar Timeout usando AWS CLI

1. **Instale a AWS CLI** (se ainda não estiver instalado):
   - Siga as instruções de instalação aqui: [AWS CLI Installation](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)
2. **Atualize a Configuração da Função**:
   - Use o comando `update-function-configuration` para alterar o valor de timeout. Exemplo:

     ```bash
      aws lambda update-function-configuration \
        --function-name my-function \
        --timeout 120
     ```

   - Substitua `my-function` pelo nome da sua função e `120` pelo valor desejado em segundos.

## Configurar Timeout usando AWS SAM

1. **Prepare o Arquivo template.yaml**:
   - Atualize o arquivo `template.yaml` do seu projeto para incluir a propriedade `Timeout`.

     ```yaml
      AWSTemplateFormatVersion: '2010-09-09'
      Transform: AWS::Serverless-2016-10-31
      Description: An AWS Serverless Application Model template describing your function.
      Resources:
        my-function:
          Type: AWS::Serverless::Function
          Properties:
            CodeUri: .
            Description: ''
            MemorySize: 128
            Timeout: 120
            # Other function properties...
     ```

2. **Implante a Função**:
   - Execute o comando `sam deploy` para aplicar as mudanças.

## Dicas para Determinar o Valor de Timeout

- **Teste com Dados Reais**: Certifique-se de que seus testes refletem o tamanho e a quantidade de dados esperados em produção.
- **Considere Latências Externas**: A interação com outros serviços pode aumentar o tempo de execução.
- **Monitore e Ajuste**: Monitore o desempenho da função em produção e ajuste o valor de timeout conforme necessário.
