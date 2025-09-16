# Projeto Loja de Eletrônicos

Este é um sistema de gerenciamento de loja de eletrônicos desenvolvido no segundo semestre de 2024 com Python, Flask, SQLAlchemy e PostgreSQL, com interface web em HTML e CSS. 

## Funcionalidades
Cadastro de Produtos: Adicione novos produtos ao estoque com nome, descrição, preço e quantidade.

Consulta de Estoque: Visualize todos os produtos disponíveis e suas quantidades

Venda de Produtos: Realize vendas e atualize automaticamente o estoque

## Tecnologias Utilizadas
Backend: Python 3.x, Flask, SQLAlchemy

Banco de Dados: PostgreSQL

Frontend: HTML, CSS

Templates: Jinja2

## Pré-requisitos
Antes de executar o projeto, certifique-se de ter instalado:

Python 3.8 ou superior

PostgreSQL

pip (gerenciador de pacotes do Python)

## Como Baixar e Executar o Projeto
-Clone ou Baixe o Projeto
```console
git clone <url>
cd projeto_loja_eletronicos
```

-Configure o Ambiente Virtual
```console
python -m venv venv
```

-Ative o ambiente virtual
 Windows:
```console
venv\Scripts\activate
```
 Linux/Mac:
```console
source venv/bin/activate
```

-Instale as Dependências
```console
pip install -r requirements.txt
```
Se não houver um arquivo requirements.txt, instale manualmente:
```console
pip install 
```
-Acesse a Aplicação
```console
flask run
```
Abra seu navegador e visite: http://localhost:5000

## Estrutura do Projeto

projeto_loja_eletronicos/
│
├── app.py                 # Arquivo principal da aplicação Flask
├── routes.py 
├── forms.py 
├── models.py              # Definição dos modelos do SQLAlchemy
├── templates/             # Templates HTML        
│   ├── index.html        
│   ├── cadastro.html   
│   ├── editar_produto.html  
│   ├── consulta.html      
│   └── venda.html      
├── static/               # Arquivos estáticos (CSS, JS, imagens)
│   ├── style.css         
│   └── relatorio.css
├── requirements.txt      # Dependências do projeto
└── .env                  # Variáveis de ambiente (não versionado)

## Rotas Disponíveis
GET / - Página inicial

GET /cadastrar - Formulário de cadastro de produtos

POST /cadastrar - Processa o cadastro de produtos

GET /estoque - Consulta todo o estoque

GET /vender - Formulário de venda

POST /vender - Processa a venda de produtos

## Licença
Este projeto é para fins educacionais.