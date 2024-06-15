# Criar um Bot da AWS Lex com Integração ao Slack

Este guia fornece instruções detalhadas sobre como criar e configurar um bot AWS Lex integrado ao Slack.

## Criar um Workspace no Slack
Acesse a pagina do [Slack Get Started](https://slack.com/get-started#landing) e siga as instruções para criar um _workspace_

## Criar um App no Slack
Acesse a pagina do [Slack API Apps][(https://slack.com/get-started#landing](https://api.slack.com/apps)) e elique em "Create New App" para criar um novo app.

## Obter Credenciais do Slack
No painel do seu app no Slack, vá para `App Credentials`, anote _Anote o Client ID_, _Client Secret_ e _Verification Token_.

![image](https://github.com/rafael-torres-nantes/Utils-Scripts/assets/58231791/8eb3e862-f151-4406-ae75-4df02e11ce24)

## Configurar Integração no AWS Lex
No console do AWS Lex, acesse o bot criado e acesse `Deployment` > `Channel integrations`.

Selecione `Slack` e insira o _Client ID_, _Client Secret_ e _Verification_ Token nos respectivos campos.
> Certifique-se de criar `Aliases` anteriormente e configurar o idioma para `Pt-br`

## Configurar Callback
No AWS Lex, obtenha o link do __Endpoint__ e o __OAuth Endpoint__.
![image](https://github.com/rafael-torres-nantes/Utils-Scripts/assets/58231791/b96d01e3-15f5-4ae2-8793-69f9380c8de0)

Retorne ao painel do Slack e siga para `OAuth & Permissions`

## Slack App: OAuth & Permissions
No campo `Redirect URLs`, adicione o __OAuth Endpoint do AWS Lex__ e salve as alterações.

Em `Scopes`, clique em `Add an OAuth Scope` e selecione:
| OAuth Scope            | Description              |
|------------------------|---------------------------|
| chat:write             | Send messages as @PizzaBot|
| team:read              | View the name, email domain, and icon for workspaces PizzaBot is connected to |
| im:history             | View messages and other content in direct messages that PizzaBot has been added to|


## Slack App: Event Subscriptions
No painel do seu app no Slack, vá para `Event Subscriptions`.  Habilite `Event Subscriptions` e, no campo `Request URL`, adicione o __Endpoint do AWS Lex__.

Em `Subscribe to bot events`, clique em `Add Bot User Event` e adicione o evento: 
| OAuth Scope            | Description              |
|------------------------|---------------------------|
| message:im             | A message was posted in a direct message channel|


## Slack App: Interactivity & Shortcuts 
No painel do seu app no Slack, vá para `Interactivity & Shortcuts` e, no campo `Request URL`, adicione o __Endpoint do AWS Lex__.

## Slack App: App Home
No painel do seu app no Slack, vá para `App Home` e, no campo `Show Tabs` habilite o __Messages Tab__ (_Direct messages your app sends will show in this tab_).
