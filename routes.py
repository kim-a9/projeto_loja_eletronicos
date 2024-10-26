from dataclasses import fields
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_smorest import abort
from sqlalchemy import text
from sqlalchemy.dialects.sqlite import insert
# import sqlalchemy.orm
from forms import CadastroForm, PesquisaForm, EditarProdutoForm, VendasForm
from models import CadastroProduto
from app import db

# from models import CadastroProduto
# from db import db
# from schemas import CadastroProdutoSchema, EditarProdutoSchema

bp = Blueprint('main', __name__)

@bp.route("/")
def home():
    return render_template("index.html")

@bp.route("/cadastro", methods=['GET', 'POST'])
def cadastro():
    form = CadastroForm()
    if form.is_submitted() and form.validate(): 
        try: 
            codigoprod = form.codigoprod.data
            produto = form.produto.data
            categoria = form.categoria.data
            quantidade = form.quantidade.data

            if CadastroProduto.query.filter_by(produto=produto).first(): 
                abort(400, message='Este produto já foi cadastrado.')
                return redirect(url_for("main.cadastro"))

            cadastro = CadastroProduto(
                codigoprod=codigoprod,
                produto=produto,
                categoria=categoria,
                quantidade=quantidade
            )

            db.session.add(cadastro)
            db.session.commit()

            flash('Produto cadastrado com sucesso!')
            return redirect(url_for('main.home'))
        except KeyError:
            abort(400, message="Erro ao cadastrar produto. Por favor, verifique os campos preenchidos.")

    return render_template("cadastro.html", form=form)

@bp.route("/pesquisa", methods=['GET', 'POST'])
def pesquisa():
    form = PesquisaForm()
    produtos = CadastroProduto.query.all() 
    if not produtos:
        flash(400, message='Nenhum produto cadastrado ainda!')
        return redirect(url_for('main.pesquisa'))
    return render_template('pesquisa.html', form=form, produtos=produtos)

@bp.route("/editar_produto/<int:id>", methods=["GET", "POST"])
def editar_produto(id):
    produto = CadastroProduto.query.get(id)
    form = EditarProdutoForm()
    if form.is_submitted() and form.validate():
        try:
            produto.codigoprod = form.codigoprod.data
            produto.produto = form.produto.data
            produto.categoria = form.categoria.data
            produto.quantidade = form.quantidade.data

            if CadastroProduto.query.filter_by(codigoprod=form.codigoprod.data).first():
                db.session.commit()
                flash('Produto editado!')
                return redirect(url_for("main.pesquisa"))
            else: 
                # codprod = CadastroProduto.query.get(produto.codigoprod)
                # if form.codigoprod.data != codprod:
                codigoprod = form.codigoprod.data
                produto = form.produto.data
                categoria = form.categoria.data
                quantidade = form.quantidade.data

                cadastro = CadastroProduto(
                    codigoprod=codigoprod,
                    produto=produto,
                    categoria=categoria,
                    quantidade=quantidade
                )
                db.session.add(cadastro)
                db.session.commit()
                flash('Novo produto cadastrado!')
                return redirect(url_for("main.pesquisa"))
            

            # if CadastroProduto.query.filter_by(codigoprod=codigoprod).first():
            #     produto_exists = True
            #     if produto_exists == True:
            #         db.session.add()
            #         db.session.commit()
            #         flash('Produto editado!')
            #         return redirect(url_for("main.pesquisa"))
            #     else:
            #         codigoprod = form.codigoprod.data
            #         produto = form.produto.data
            #         categoria = form.categoria.data
            #         quantidade = form.quantidade.data

            #         cadastro = CadastroProduto(
            #             codigoprod=codigoprod,
            #             produto=produto,
            #             categoria=categoria,
            #             quantidade=quantidade
            #         )
            #         db.session.add(cadastro)
            #         db.session.commit()
            #         flash('Novo produto cadastrado!')
            #         return redirect(url_for("main.pesquisa"))
        except KeyError:
            abort(400, message="Erro ao atualizar produto. Por favor, verifique os campos preenchidos.")
            return render_template("editar_produto.html", form=form, produto=produto)
                            #upsert. Se um produto já existe, ele é atualizado. Se não, ele é criado.
    #     except KeyError:
    #         abort(400, message="Erro ao cadastrar produto. Por favor, verifique os campos preenchidos.")
    return render_template("editar_produto.html", form=form, produto=produto)

@bp.route("/excluir/<int:id>", methods=["POST"])
def excluir_produto(id):
    if request.method == 'POST':
        produto = CadastroProduto.query.get(id)
        db.session.delete(produto)
        db.session.commit()
        flash('Produto excluído do estoque!')
    return redirect(url_for('main.pesquisa'))


@bp.route("/venda", methods=['GET', 'POST'])
def venda():
    form = VendasForm()
    produto = CadastroProduto.query.all()
    if request.method == 'POST': 
        codprod = request.form.get("codigoprod","")
        cp = CadastroProduto.query.filter_by(codigoprod=codprod).first()
        if codprod > cp.quantidade:
            flash('Estoque insuficiente para a venda!')
        
        cp.quantidade = int(cp.quantidade - int(form.qtd.data))
        CadastroProduto.query.filter_by(codigoprod=codprod).update(dict(quantidade=cp.quantidade))
        try:
            db.session.commit()
            flash('Venda realizada com sucesso!')
            return redirect(url_for("main.home"))
        except KeyError:
                flash("Verifique a quantidade em estoque.")
    else: 
        flash("Verifique os campos preenchidos. ")
    return render_template('venda.html', form=form, produto=produto)

@bp.route("/relatorio", methods=['GET', 'POST'])
def relatorio():
    return render_template('relatorio.html')