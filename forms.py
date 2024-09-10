from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SubmitField
from wtforms.validators import DataRequired

class CadastroForm(FlaskForm):
  produto =  StringField('Produto', validators=[DataRequired()])
  quantidade = IntegerField('Quantidade', validators=[DataRequired()])
  preco = FloatField('Preço', validators=[DataRequired()])
  submit = SubmitField('Cadastrar')




