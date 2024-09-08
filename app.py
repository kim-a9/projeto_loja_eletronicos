# Inicialização do aplicativo, olhar documentação Flask - Layout do projeto
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Deu bom!!!"

