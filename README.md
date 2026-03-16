# Projeto Loja de Eletrônicos

Este é um sistema de gerenciamento de loja de eletrônicos desenvolvido no segundo semestre de 2024 com Python, Flask, SQLAlchemy e PostgreSQL, com interface web em HTML e CSS. 

## Funcionalidades
- **Cadastro de Produtos**: Adicione novos itens ao estoque informando código, nome, categoria e quantidade.
- **Consulta de Estoque**: Visualize todos os produtos em uma tabela clara e organizada, com indicadores visuais para itens com baixo estoque.
- **Edição de Produtos**: Modifique informações de produtos já cadastrados, como nome, categoria ou quantidade.
- **Exclusão de Produtos**: Remova itens do sistema de forma segura.
- **Registro de Vendas**: Realize a baixa de produtos do estoque de forma rápida, apenas com o código do produto e a quantidade vendida.
- **Interface Intuitiva**: Interface de usuário limpa e responsiva, construída com Bootstrap 5, garantindo uma ótima experiência em desktops e dispositivos móveis.

## Tecnologias Utilizadas
- **Backend**: Python 3.11+
- **Framework**: Flask
- **ORM**: Flask-SQLAlchemy
- **Migrações de Banco**: Flask-Migrate
- **Formulários**: Flask-WTF
- **Banco de Dados**: PostgreSQL
- **Frontend**: HTML5, CSS3, Bootstrap 5

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
Abra seu navegador e visite: http://localhost:<port>

### Outro comandos que você pode precisar
Este projeto conta com Flask Migrate para realização de migração do banco de dados. 

- Incializa as migrações: 
```console
flask db init
```
- Realize a mudança: 
```console
flask db upgrade
```
Flask vai olhar o arquivo models.py, ver a classe CadastroProduto e criar o banco a partir disso.


## Estrutura do Projeto

```
/projeto_loja_eletronicos
|-- /db/
|   |-- projeto_estokey.db   
|-- /migrations/            # Arquivos de migração do Alembic
|-- /static/
|   |-- style.css             # Folhas de estilo personalizadas
|-- /templates/
|   |-- base.html             # Template base com a estrutura principal
|   |-- cadastro.html         
|   |-- consulta.html         
|   |-- editar_produto.html   
|   |-- index.html            
|   |-- venda.html           
|-- app.py                 
|-- config.py              
|-- forms.py                
|-- models.py              
|-- routes.py               
|-- requirements.txt        
|-- README.md              
```

## Rotas Disponíveis
GET /home - Página inicial

GET /cadastro - Formulário de cadastro de produtos

POST /cadastro - Processa o cadastro de produtos

GET /consulta - Consulta todo o estoque

GET /vendas - Formulário de venda

POST /vendas - Processa a venda de produtos

## Licença
Este projeto é para fins educacionais.