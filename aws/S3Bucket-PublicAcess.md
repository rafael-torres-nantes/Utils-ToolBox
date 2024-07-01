# Como Deixar uma Pasta S3 com Acesso Público

Este guia irá mostrar como configurar uma pasta (bucket) no Amazon S3 para que seus arquivos possam ser acessados publicamente. 

## Passo 1: Acessar o Console da AWS

1. Acesse o console da AWS: [AWS Management Console](https://aws.amazon.com/console/)
2. Faça login com suas credenciais.

## Passo 2: Navegar até o S3

1. No console da AWS, procure por "S3" no campo de busca e clique no serviço Amazon S3.

## Passo 3: Criar ou Selecionar um Bucket

1. Se você já possui um bucket que deseja tornar público, selecione-o na lista.
2. Caso contrário, clique em "Create bucket" para criar um novo bucket. Dê um nome único ao seu bucket e escolha a região desejada.

## Passo 4: Configurar Permissões do Bucket

1. Selecione o bucket desejado.
2. Clique na aba "Permissions".
3. Em "Block Public Access (bucket settings)", clique em "Edit" e desabilite todas as opções. Confirme a desativação.

![S3-PublicAcess-Part1](https://github.com/rafael-torres-nantes/Utils-ToolBox/assets/58231791/319294e8-fa6e-4f39-a96f-4e2aa27d5b16)

## Passo 5: Adicionar a Política de Bucket

1. Ainda na aba "Permissions", role para baixo até encontrar "Bucket Policy" e clique em "Edit".

![S3-PublicAcess-Part2](https://github.com/rafael-torres-nantes/Utils-ToolBox/assets/58231791/28634dd5-a03b-4f2c-9644-5af905f6fb56)
![S3-PublicAcess-Part3](https://github.com/rafael-torres-nantes/Utils-ToolBox/assets/58231791/74da7ea4-ce5d-4385-be92-16253598237c)

2. Adicione a seguinte política de bucket e clique em "Save":

```json
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Sid": "Statement1",
			"Principal": "*",
			"Effect": "Allow",
			"Action": [
				"s3:GetObject"
			],
			"Resource": [
				"arn:aws:s3:::sprint08-my-photos/*",
				"arn:aws:s3:::sprint08-my-photos/*"
			]
		}
	]
}
```

Essa política permite que qualquer pessoa (Principal: "*") possa acessar os objetos no bucket especificado ("sprint08-my-photos").

## Passo 6: Confirmar Permissões dos Objetos

1. Clique na aba "Objects" dentro do seu bucket.
2. Selecione os arquivos ou pastas que deseja tornar públicos.
3. Clique em "Actions" e depois em "Make public".

## Verificação Final

Para garantir que tudo está funcionando corretamente, acesse um dos arquivos no seu bucket usando a URL pública no formato:

```
https://sprint08-my-photos.s3.amazonaws.com/nome-do-arquivo
```

Se o arquivo for exibido corretamente, então a configuração de acesso público foi realizada com sucesso.

Mais informações da [documentação oficial da AWS sobre permissões de bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-bucket-policies.html)
