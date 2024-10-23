from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class CadastroForm(FlaskForm):
    codigoprod = IntegerField('Código:', validators=[DataRequired()])
    produto = StringField('Produto:', validators=[DataRequired()])
    categoria = StringField('Categoria:')
    quantidade = IntegerField('Quantidade:')
    submit = SubmitField('Cadastrar')

class PesquisaForm(FlaskForm):
    produto = StringField('Pesquisar por nome do produto: ', validators=[DataRequired()])
    submit = SubmitField('Buscar')

class EditarProdutoForm(FlaskForm):
    codigoprod = IntegerField('Código')
    produto = StringField('Produto: ', validators=[DataRequired()])
    categoria = StringField('Categoria: ')
    quantidade = IntegerField('Quantidade: ', validators={DataRequired()})
    submit = SubmitField('Editar')

class VendasForm(FlaskForm):
    codigo = IntegerField('Código da Venda:', validators=[DataRequired()])
    codigoprod = IntegerField('Código do  Produto:', validators=[DataRequired()])
    produto = StringField('Produto:', validators=[DataRequired()])
    qtd = IntegerField('Quantidade:', validators=[DataRequired()])
    submit = SubmitField('Registrar Venda')



