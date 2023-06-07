# Integrando chatGPT com o Python

Primeiro crie seu token :

```
acesse: https://openai.com/
Crie um user (Sign up) ou acesse sua conta (Log in)
clique em :
API
Personal
View API keys
Create new secret key (dê um nome e salve esta chave)

verifique seu uso trial:
https://platform.openai.com/account/usage

```

criar o arquivo de variáveis .env
```
OPENAI.API_KEY='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

```

no terminal:
```bash
python3 -m venv env
source env/bin/activate
pip install openai
pip install python-dotenv
python3 chatGPT.py
```


### se tiver problema com o python no vscode

pressione CTRL + Shift + P e selecione o python correto