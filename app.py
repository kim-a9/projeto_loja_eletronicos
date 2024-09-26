# Inicialização do aplicativo, olhar documentação Flask - Layout do projeto
from flask import Flask
from flask import render_template, request, redirect, url_for, flash
from forms import CadastroForm


app = Flask(__name__)



@app.route("/")
def home():
    return render_template('/index.html')

@app.route("/cadastro.html", methods =['GET', 'POST'])
def cadastro():
    form = CadastroForm()
    if form.is_submitted():
       flash('Produto cadastrado!')
       return redirect(url_for('/index.html'))
    return render_template('/cadastro.html', form=form)








if __name__ == '__main__':
    app.run(debug=True)
