# Instalação do WSL

## Passo 1: Instalar o WSL

Execute o seguinte comando para instalar o Windows Subsystem for Linux:

```bash
wsl.exe --install
```

Este comando instala a versão mais recente do WSL junto com a distribuição padrão (geralmente o Ubuntu).

---

## Passo 2: Listar distribuições disponíveis

Para visualizar todas as distribuições Linux disponíveis para instalação, use:

```bash
wsl.exe --list --online
```

A saída exibirá uma lista de distribuições, como:

```
NAME                            FRIENDLY NAME
Ubuntu                          Ubuntu
Debian                          Debian GNU/Linux
kali-linux                      Kali Linux Rolling
Ubuntu-22.04                    Ubuntu 22.04 LTS
openSUSE-Tumbleweed             openSUSE Tumbleweed
...
```

---

## Passo 3: Instalar uma distribuição específica

Substitua `<Distro>` pelo nome da distribuição desejada. Por exemplo, para instalar o **Ubuntu 24.04**, use:

```bash
wsl.exe --install Ubuntu-24.04
```

---
