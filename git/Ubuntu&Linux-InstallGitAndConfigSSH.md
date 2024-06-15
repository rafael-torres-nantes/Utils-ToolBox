# Instalação do Git e Configuração de Chave SSH

Este guia descreve como instalar o Git e configurar uma chave SSH para autenticação no GitHub em diferentes distribuições Linux.

## Passo 1: Instalar o Git

### No Ubuntu
Abra o terminal e execute o seguinte comando:
```bash
sudo apt install git
```

### No Fedora/CentOS
Abra o terminal e execute o seguinte comando:
```bash
sudo yum install git
```

## Passo 2: Gerar uma Chave SSH

Para gerar uma nova chave SSH, execute o comando abaixo no terminal, substituindo `XXXXXXX@gmail.com` pelo seu endereço de e-mail:
```bash
ssh-keygen -t rsa -b 4096 -C "XXXXXXX@gmail.com"
```

### Passo 2.1: Copiar a Chave Pública

Para copiar a chave pública gerada, execute o seguinte comando:
```bash
cat ~/.ssh/id_rsa.pub
```
**Nota:** Copie o código impresso no terminal. Este é o seu SSH Key.

## Passo 3: Adicionar a Chave SSH ao GitHub

1. Vá para [GitHub](https://github.com) e faça login na sua conta.
2. Clique no seu avatar no canto superior direito e selecione `Settings`.
3. No menu à esquerda, clique em `SSH and GPG keys`.
4. Clique no botão `New SSH Key`.
5. Cole sua chave pública no campo "Key" e dê um título significativo.

## Passo 4: Clonar o Repositório via SSH

Agora você pode clonar o repositório usando SSH. Execute o seguinte comando no terminal, substituindo `XXXXXXXXXXX` pelo caminho do seu repositório no GitHub:
```bash
git clone git@github.com:XXXXXXXXXXX
```
