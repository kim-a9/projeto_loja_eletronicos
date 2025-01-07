from dataclasses import fields
from flask import Blueprint, make_response, render_template, request, redirect, url_for, flash
from flask_smorest import abort
import pdfkit
from forms import CadastroForm, EditarProdutoForm, VendasForm
from models import CadastroProduto
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

            if CadastroProduto.query.filter_by(produto=produto).first(): 
                flash('Este produto já foi cadastrado.')
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
            abort(400, message="Erro ao cadastrar produto. Por favor, verifique os campos preenchidos.")

    return render_template("cadastro.html", form=form)

@bp.route("/consulta", methods=['GET', 'POST'])
def consulta():
    produtos = CadastroProduto.query.order_by(CadastroProduto.codigoprod)
    if not produtos:
        flash(f'Nenhum produto cadastrado ainda!')
        return redirect(url_for('main.consulta'))
    return render_template('consulta.html', produtos=produtos)

@bp.route("/editar_produto/<int:id>,<int:codigoprod>", methods=["GET", "POST"])
def editar_produto(id, codigoprod):
    produto = CadastroProduto.query.get(id)
    form = EditarProdutoForm()

    if form.is_submitted() and form.validate():
        try:
            produto.codigoprod = form.codigoprod.data
            produto.produto = form.produto.data
            produto.categoria = form.categoria.data
            produto.quantidade = form.quantidade.data

            if CadastroProduto.query.filter_by(codigoprod=codigoprod).first(): 
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
                db.session.commit()
                flash('Produto editado!')
                redirect(url_for("main.consulta"))            
                try:
                    db.session.add(cadastro)
                    db.session.commit()
                    flash('Novo produto cadastrado!')
                    redirect(url_for("main.consulta"))
                except Exception as e:
                    flash(f"Ocorreu um erro: {str(e)}", "error")
                    db.session.rollback()
        except KeyError:
            abort(400, message="Erro ao atualizar produto. Por favor, verifique os campos preenchidos.")
            return render_template("consulta.html", produtos=produtos)
    return render_template("editar_produto.html", form=form, produto=produto)

@bp.route("/excluir/<int:id>", methods=["POST"])
def excluir_produto(id):
    if request.method == 'POST':
        produto = CadastroProduto.query.get(id)
        db.session.delete(produto)
        db.session.commit()
        flash('Produto excluído do estoque!')
    return redirect(url_for('main.consulta'))


@bp.route("/venda", methods=['GET', 'POST'])
def venda():
    form = VendasForm()
    produto = CadastroProduto.query.all()
    if request.method == 'POST': 
        try:
            codprod = request.form.get("codigoprod","")
            cp = CadastroProduto.query.filter_by(codigoprod=codprod).first()
            cp.quantidade = int(cp.quantidade - int(form.qtd.data))
            CadastroProduto.query.filter_by(codigoprod=codprod).update(dict(quantidade=cp.quantidade))
            
            db.session.commit()
            flash('Venda realizada com sucesso!')
            return redirect(url_for("main.venda"))
        except Exception as e:
            flash(f"Ocorreu um erro: {str(e)}", "error")
            db.session.rollback()

    return render_template('venda.html', form=form, produto=produto)

@bp.route("/relatorio", methods=['GET', 'POST'])
def relatorio():
    totalprod = CadastroProduto.query.count()
    produtos = CadastroProduto.query.order_by(CadastroProduto.codigoprod)
    qnt = CadastroProduto.query.filter_by(quantidade='0').all()

    qnt_report = [{"produto": p.produto, "quantidade": p.quantidade} for p in qnt]

    try:
        r = render_template('relatorio.html', totalprod=totalprod, produtos=produtos, qnt=qnt, qnt_report=qnt_report)
        css = ['static/relatorio.css']
        pdf = pdfkit.from_string(r, False, css=css)

        response = make_response(pdf)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = f'attachment; filename="relatorio.pdf"'
        return response
    except Exception:
        flash(f'Não foi possível gerar o relatório')
        return redirect(url_for('main.home'))

    # return render_template('relatorio.html', totalprod=totalprod, produtos=produtos, qnt=qnt, qnt_report=qnt_report)