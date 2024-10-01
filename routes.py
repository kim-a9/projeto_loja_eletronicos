from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_smorest import abort
from forms import CadastroForm, VendasForm
# from models import CadastroProduto, Vendas
# from . import db


bp = Blueprint('main', __name__)

@bp.route("/")
def home():
    return render_template("index.html")


@bp.route("/cadastro", methods=['GET', 'POST'])
def cadastro():
    form = CadastroForm()
    if form.is_submitted() and form.validate():
        # codigoprod = form.codigoprod.data
        # produto = form.produto.data
        # categoria = form.categoria.data
        # quantidade = form.quantidade.data

        # if CadastroProduto.query.filter_by(produto=produto).first(): 
        #     flash('Produto já cadastrado')
        #     return redirect(url_for(cadastro.html))

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
    
    return render_template("cadastro.html", form=form)

@bp.route("/pesquisa", methods=['GET', 'POST'])
def pesquisa():
    # try:
    #     if request.method == 'POST': 
    #         produtos = CadastroProduto.query.all()
    #         if not produtos:
    #             flash('Nenhum produto cadastrado ainda!')
    #             return redirect(url_for('pesquisa'))
    # except KeyError:
    #     abort(404, description='Produto não encontrado. Verifique os campos preenchidos')
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