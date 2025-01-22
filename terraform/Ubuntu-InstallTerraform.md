# Instalação do Terraform

## Passo 1: Importar a chave GPG

Baixe e importe a chave pública GPG do HashiCorp:

```bash
wget -O - https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
```

---

## Passo 2: Adicionar o repositório do HashiCorp

Adicione o repositório ao gerenciador de pacotes:

```bash
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
```

---

## Passo 3: Atualizar e instalar o Terraform

Atualize a lista de pacotes e instale o Terraform:

```bash
sudo apt update && sudo apt install terraform
```

---
