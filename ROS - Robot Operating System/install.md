# Guia de Instalação do ROS

Este guia irá te ajudar a instalar o ROS 2 (Robot Operating System) no Ubuntu. Siga os passos abaixo para configurar o ROS no seu sistema.

## Passo 1: Verificar Configuração de Localização UTF-8

Certifique-se de que a localização do seu sistema está configurada para usar UTF-8. Isso é importante para a instalação do ROS.

```bash
sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8
```

Verifique as configurações de localização:

```bash
locale
```

## Passo 2: Instalar Pacotes Necessários

Instale os pacotes necessários e adicione o repositório Universe se ainda não estiver adicionado.

```bash
sudo apt install software-properties-common
sudo add-apt-repository universe
```

## Passo 3: Configurar o Repositório do ROS 2

Adicione a chave do repositório do ROS 2 e configure o repositório.

```bash
sudo apt update && sudo apt install curl -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
```

#### Passo 4: Instalar o ROS 2

Atualize o índice de pacotes e instale os pacotes do ROS 2. Substitua `ros-humble-desktop` e `ros-humble-ros-base` pela distribuição específica do ROS e pelos pacotes que você precisa.

```bash
sudo apt update
sudo apt upgrade -y
sudo apt install ros-humble-desktop  # Substitua pela distribuição do ROS desejada
sudo apt install ros-humble-ros-base  # Substitua pela distribuição do ROS desejada
```

#### Passo 5: Instalar Ferramentas de Desenvolvimento do ROS (Opcional)

Instale ferramentas adicionais de desenvolvimento do ROS, se necessário.

```bash
sudo apt install ros-dev-tools
```

#### Passo 6: Configurar o Ambiente

Adicione a configuração do ambiente do ROS ao arquivo de configuração do seu shell (por exemplo, `~/.bashrc`).

```bash
echo "source /opt/ros/<sua_distribuicao_ros>/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

Substitua `<sua_distribuicao_ros>` pela distribuição do ROS que você instalou (por exemplo, `foxy`, `galactic`, etc.).

## Passo 7: Verificar a Instalação

Verifique a instalação do ROS verificando as variáveis de ambiente do ROS e testando com comandos básicos do ROS.

```bash
printenv | grep ROS
ros2 doctor
```

# Notas Adicionais

- Substitua `<sua_distribuicao_ros>` ao longo do guia pela distribuição do ROS que você está instalando (por exemplo, `foxy`, `galactic`, etc.).
- Ajuste os nomes dos pacotes (`ros-humble-desktop`, `ros-humble-ros-base`, etc.) de acordo com a distribuição específica do ROS e os requisitos dos pacotes.

Agora, a instalação do ROS deve estar completa e pronta para uso no seu sistema Ubuntu.
