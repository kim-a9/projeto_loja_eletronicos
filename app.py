from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from forms import CadastroForm, VendasForm
# from models import CadastroProduto
# from . import db

app = Flask(__name__)

app.config['SECRET_KEY'] = 'admin123'
# app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///projeto_loja_eletronicos.db'

# db = SQLAlchemy(app)

    
@app.route("/")
def home():
    return render_template('/index.html')


@app.route("/cadastro", methods=['GET', 'POST'])
def cadastro():
    form = CadastroForm()
    if form.is_submitted() and form.validate():
        # codigoprod = form.codigoprod.data
        # produto = form.produto.data
        # categoria = form.categoria.data
        # quantidade = form.quantidade.data

        # cadastro = CadastroProduto(
        #     codigoprod=codigoprod,
        #     produto=produto,
        #     categoria=categoria,
        #     quantidade=quantidade
        # )

        # db.session.add(cadastro)
        # db.session.commit()

        flash('Produto cadastrado com sucesso!')
        return redirect(url_for('home'))
    return render_template('cadastro.html', form=form)

@app.route("/pesquisa", methods=['GET', 'POST'])
def pesquisa():
    return render_template('pesquisa.html')

@app.route("/venda", methods=['GET', 'POST'])
def venda():
    form = VendasForm()
    if form.is_submitted() and form.validate():
        return redirect(url_for('home'))
    flash('Venda registrada com sucesso!')
    return render_template('venda.html', form=form)

@app.route("/relatorio", methods=['GET', 'POST'])
def relatorio():
    return render_template('relatorio.html')





if __name__ == '__main__':
    app.run(debug=True)
