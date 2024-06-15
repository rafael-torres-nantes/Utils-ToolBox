# Instalação do AWS CLI no Ubuntu

Este guia descreve como instalar a AWS CLI (Command Line Interface) no Ubuntu.

## Passo 1: Baixar a AWS CLI

### Baixar o instalador da AWS CLI
Abra o terminal e execute o seguinte comando para baixar o arquivo zip do instalador:
```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
```

## Passo 2: Descompactar o Arquivo Zip

### Descompactar o arquivo zip baixado
Execute o comando abaixo para descompactar o arquivo:
```bash
unzip awscliv2.zip
```

## Passo 3: Instalar a AWS CLI

### Executar o instalador
Para instalar a AWS CLI, execute o comando a seguir:
```bash
sudo ./aws/install
```

## Passo 4: Verificar a Instalação

### Verificar a versão da AWS CLI
Para garantir que a AWS CLI foi instalada corretamente, verifique a versão instalada:
```bash
aws --version
```

### Documentação Oficial

Para mais informações e detalhes adicionais, consulte a [documentação oficial da AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html).
