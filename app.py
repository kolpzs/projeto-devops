from flask import Flask

# 1. Cria a nossa aplicação web
app = Flask(__name__)

# 2. Define o que acontece quando alguém acessa a página principal
@app.route("/")
def hello_world():
    # 3. Retorna a mensagem que será exibida no navegador
    return "<h1>Olá, Mundo! Bem-vindo ao nosso projeto.</h1>"