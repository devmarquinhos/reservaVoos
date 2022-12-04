from flask import Flask # Importando o Flask
from flask_sqlalchemy import SQLAlchemy # Importando a biblioteca da ORM SQL do Flask

app = Flask(__name__) # Inicializando a aplicação
app.config['SQLAlchemy_DATABASE_URI'] = 'sqlite:///storage.db' # Configurando a URI de conexão do banco de dados
db = SQLAlchemy(app) # Criando o banco de dados

from app.controllers import default # Importando as routes do Flask
