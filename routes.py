from flask import Blueprint, render_template, request, redirect, url_for, flash
from forms import CadastroForm, VendasForm
from models import CadastroProdutos, Vendas

bp = Blueprint('main', __name__)

@bp.route("/")
def home():
    return render_template('/index.html')


@bp.route("/cadastro", methods=['GET', 'POST'])
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

@bp.route("/pesquisa", methods=['GET', 'POST'])
def pesquisa():
    return render_template('pesquisa.html')

@bp.route("/venda", methods=['GET', 'POST'])
def venda():
    form = VendasForm()
    if form.is_submitted() and form.validate():
        return redirect(url_for('home'))
    flash('Venda registrada com sucesso!')
    return render_template('venda.html', form=form)

@bp.route("/relatorio", methods=['GET', 'POST'])
def relatorio():
    return render_template('relatorio.html')