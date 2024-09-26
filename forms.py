from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SubmitField
from wtforms.validators import DataRequired

class CadastroForm(FlaskForm):
    codigo = IntegerField('Código', validators=[DataRequired()])
    produto = StringField('Produto', validators=[DataRequired()])
    categoria = StringField('Categoria', validators=[DataRequired()])
    quantidade = IntegerField('Quantidade', validators=[DataRequired()])
    submit = SubmitField('Cadastrar')
