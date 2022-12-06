from flask import Flask # Importando o Flask
from flask_sqlalchemy import SQLAlchemy # Importando a biblioteca da ORM SQL do Flask
from flask_migrate import Migrate # Importando a biblioteca responsável pelas migrations do banco de dados

app = Flask(__name__) # Inicializando a aplicação
app.config.from_object('config') # Passando as config. para o Flask deixando o arquivo de configurações separado
db = SQLAlchemy(app) # Criando o banco de dados
migrate = Migrate(app, db) # Instancia para o Migrate cuidar da aplicação, recebendo tanto a aplicação quanto o banco de dados


from app.controllers import default # Importando as routes do Flask
