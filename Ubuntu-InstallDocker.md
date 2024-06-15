# Instalação do Docker no Ubuntu

Este guia descreve como instalar o Docker no Ubuntu utilizando o repositório apt oficial do Docker.

## Passo 1: Preparação do Sistema

### Atualizar o sistema e instalar dependências
Abra o terminal e execute os seguintes comandos:
```bash
sudo apt-get update
sudo apt-get install ca-certificates curl
```

### Adicionar a chave GPG oficial do Docker
Crie um diretório para armazenar a chave e faça o download da chave GPG:
```bash
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```

### Adicionar o repositório do Docker às fontes do apt
Adicione o repositório usando o comando abaixo:
```bash
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

## Passo 2: Instalar os Pacotes do Docker

### Instalar Docker Engine, CLI e outros pacotes
Execute o comando a seguir para instalar os pacotes do Docker:
```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

## Passo 3: Verificar a Instalação do Docker

### Verificar a versão do Docker
Para garantir que o Docker foi instalado corretamente, verifique a versão instalada:
```bash
docker --version
```

### Rodar a imagem de teste hello-world
Para confirmar que a instalação foi bem sucedida, execute a imagem `hello-world`:
```bash
docker run hello-world
```

### Documentação Oficial

Para mais informações e detalhes adicionais, consulte a [documentação oficial do Docker](https://docs.docker.com/engine/install/ubuntu/).

---

Este README fornece instruções claras e detalhadas para a instalação do Docker no Ubuntu, garantindo que os usuários possam seguir cada passo com facilidade.
