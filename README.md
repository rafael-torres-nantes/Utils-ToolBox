# 🔧Utils-ToolBox

## 👨‍💻 Projeto desenvolvido por: 
[Rafinha](https://github.com/rafael-torres-nantes)

## Índice

* 📚 Contextualização do projeto
* 🛠️ Tecnologias/Ferramentas utilizadas
* 📁 Estrutura do projeto
* 📌 Como executar o projeto

## 📚 Contextualização do projeto

O Utils-ToolBox é uma iniciativa para consolidar conhecimentos e facilitar o acesso a informações vitais para desenvolvedores e entusiastas da tecnologia. Com uma abordagem prática e direta, buscamos oferecer recursos que permitam a implementação eficiente de soluções em diversos ambientes e com múltiplas ferramentas.

Aprender e utilizar esses recursos abre as portas para um mundo de possibilidades criativas e profissionais. Com o conteúdo deste repositório, você poderá:
- __Implementar ambientes de desenvolvimento e produção:__ configuração de ferramentas essenciais como Docker, AWS CLI, entre outros.
- __Automatizar e otimizar processos:__ scripts e tutoriais para agilizar seu fluxo de trabalho.
- __Garantir a segurança e confiabilidade dos dados:__ boas práticas e ferramentas para validação e proteção de informações.
- __Explorar uma gama de frameworks e bibliotecas:__ ferramentas que facilitam o desenvolvimento e expandem as funcionalidades de seus projetos.

## 🛠️ Tecnologias/Ferramentas utilizadas

[<img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white">](https://www.python.org/)
[<img src="https://img.shields.io/badge/Visual_Studio_Code-007ACC?logo=visual-studio-code&logoColor=white">](https://code.visualstudio.com/)
[<img src="https://img.shields.io/badge/AWS-FF9900?logo=amazonaws&logoColor=white">](https://aws.amazon.com/)
[<img src="https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white">](https://www.docker.com/)
[<img src="https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white">](https://git-scm.com/)
[<img src="https://img.shields.io/badge/WSL-4EAA25?logo=linux&logoColor=white">](https://docs.microsoft.com/en-us/windows/wsl/)
[<img src="https://img.shields.io/badge/ROS-22314E?logo=ros&logoColor=white">](https://www.ros.org/)
[<img src="https://img.shields.io/badge/Terraform-623CE4?logo=terraform&logoColor=white">](https://www.terraform.io/)

## 📁 Estrutura do projeto

A estrutura do projeto é organizada da seguinte maneira:

```
.
├── AWS - Amazon Web Services/
│   ├── Lambda-IncreaseTimeoutTime.md
│   ├── LexAWS-ConnectionSlack.md
│   ├── S3Bucket-PublicAcess.md
│   ├── services/
│   │   ├── utils/
│   │   │   ├── check_login_aws.py
│   │   │   ├── import_credentials.py
│   │   ├── ClassDynamoDB.py
│   │   ├── ClassAWSPolly.py
│   ├── Ubuntu-InstallAWS.md
│   ├── Ubuntu-InstallServerlessCLI.md
├── Docker/
│   ├── Ubuntu-InstallDocker.md
├── Git/
│   ├── Ubuntu&Linux-InstallGitAndConfigSSH.md
├── LICENSE
├── README.md
├── ROS - Robot Operating System/
│   ├── install-ros.sh
│   ├── install.md
├── Terraform/
│   ├── Ubuntu-InstallTerraform.md
├── test_files/
│   ├── teste.txt
├── Utill Python/
│   ├── cuda_check.py
│   ├── get_text_webpage.py
│   ├── request_api.py
│   ├── timer_count.py
├── WSL/
│   ├── InstallWSL.md
```

## 📌 Como executar o projeto

Para executar o projeto localmente, siga as instruções abaixo:

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/rafael-torres-nantes/utils-toolbox.git
   ```

2. **Instale as dependências necessárias:**
   - Para scripts Python, instale as dependências listadas nos arquivos correspondentes.

3. **Execute os scripts conforme necessário:**
   - Siga as instruções nos arquivos 

README.md

 e nos scripts individuais para configurar e executar cada ferramenta ou serviço.

## 🕵️ Dificuldades Encontradas

Durante o desenvolvimento do projeto, algumas dificuldades foram enfrentadas, como:

- **Integração com serviços AWS:** O uso de credenciais e permissões para acessar os serviços da AWS exigiu cuidados especiais para garantir a segurança e funcionalidade do sistema.
- **Configuração de ambientes:** A configuração de diferentes ambientes de desenvolvimento e produção, especialmente ao lidar com múltiplas ferramentas e tecnologias, foi um desafio contínuo.
- **Automatização de processos:** A criação de scripts eficientes para automatizar tarefas e otimizar o fluxo de trabalho exigiu testes e ajustes constantes.