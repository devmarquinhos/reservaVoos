import os.path
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'storage.db') # Configurando a URI de conexão do banco de dados
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = 'um-nome-bem-seguro'