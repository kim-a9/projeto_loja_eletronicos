from flask import Flask, render_template, request, redirect, url_for, flash
from forms import CadastroForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'admin123'

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/cadastro", methods=['GET', 'POST'])
def cadastro():
    form = CadastroForm()
    if form.is_submitted() and form.validate():
        flash('Produto cadastrado com sucesso!')
        return redirect(url_for('home'))
    return render_template('cadastro.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
