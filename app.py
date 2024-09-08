# Inicialização do aplicativo, olhar documentação Flask - Layout do projeto
from flask import Flask
from flask import render_template, request, redirect, url_for, flash


app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/cadastro", methods =['GET', 'POST'])
def cadastro():
#    if request.method == 'POST':
#        flash('Produto cadastrado!')
#        return redirect(url_for('index.html'))
    return render_template('cadastro.html')



