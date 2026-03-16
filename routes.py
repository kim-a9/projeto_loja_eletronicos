from dataclasses import fields
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_smorest import abort
from forms import CadastroForm, EditarProdutoForm, VendasForm
from models import CadastroProduto
from flask_sqlalchemy import SQLAlchemy
from app import db


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

            if CadastroProduto.find_by_cod(codigoprod=form.codigoprod.data): 
                flash('Já existe um produto com o código {form.codigoprod.data}.', 'danger')
                return redirect(url_for("main.cadastro"))
            
            if CadastroProduto.query.filter_by(produto=form.produto.data).first(): 
                flash('Este produto já foi cadastrado.', 'danger')
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
            return redirect(url_for('main.cadastro'))
        except KeyError:
            db.session.rollback()
            abort(400, message="Erro ao cadastrar produto. Por favor, verifique os campos preenchidos. {str(e)}")

    return render_template("cadastro.html", form=form)

@bp.route("/consulta", methods=['GET', 'POST'])
def consulta():
    produtos = CadastroProduto.query.order_by(CadastroProduto.codigoprod)
    if not produtos:
        flash(f'Nenhum produto cadastrado ainda!')
        return redirect(url_for('main.consulta'))
    return render_template('consulta.html', produtos=produtos)

@bp.route("/editar_produto/<int:id>,<int:codigoprod>", methods=['GET', 'POST'])
def editar_produto(id, codigoprod):
    produto = CadastroProduto.query.get(id)
    form = EditarProdutoForm(obj=produto)

    if form.is_submitted() and form.validate():
        outroprod = CadastroProduto.query.filter(
            CadastroProduto.codigoprod == form.codigoprod.data,
            CadastroProduto.id != id).first()
        
        if outroprod: 
            flash(f'O código {form.codigoprod.data} já está em uso', 'danger')
            return render_template("editar_produto.html", form=form, produto=produto)
        
        try:
            produto.codigoprod = form.codigoprod.data
            produto.produto = form.produto.data
            produto.categoria = form.categoria.data
            produto.quantidade = form.quantidade.data

            
            db.session.commit()
            flash('Produto editado!', 'success')
            return redirect(url_for("main.consulta"))    

        except Exception as e:
            db.session.rollback()
            flash(f"Ocorreu um erro ao salvar: {str(e)}", "danger")
         
    return render_template("editar_produto.html", form=form, produto=produto)

@bp.route("/excluir/<int:id>", methods=['POST'])
def excluir_produto(id):
    if request.method == 'POST':
        produto = CadastroProduto.query.get(id)
        db.session.delete(produto)
        db.session.commit()
        flash('Produto excluído do estoque!', 'success')
    return redirect(url_for('main.consulta'))

@bp.route("/venda", methods=['GET', 'POST'])
def venda():
    form = VendasForm()
    produto = CadastroProduto.query.all()
    if request.method == 'POST': 
        produto = CadastroProduto.find_by_cod(form.codigoprod.data)
        
        if not produto: 
            flash(f'Produto com código {form.codigoprod.data} não foi encontrado.', 'danger')
            return render_template('venda.html', form=form)
        
        if produto.quantidade < form.qtd.data:
            flash(f'Estoque insuficiente! Disponível: {produto.quantidade}', 'warning')
            return render_template('venda.html', form=form)
        
        try:
            produto.quantidade -= form.qtd.data
            db.session.commit()
            flash(f'Venda de {form.qtd.data} unidades de "{produto.produto}" registrada com sucesso!', 'success')
            return redirect(url_for("main.venda"))
        except Exception as e:
            db.session.rollback()
            flash(f"Ocorreu um erro: {str(e)}", "error")

    return render_template('venda.html', form=form, produto=produto)

