from app import db # Importando o banco de dados, do __init__ na pasta-mãe app

class User(db.Model): # Criando a tabela de users usando uma padrão do Flask
    __tablename__ = "users" # Setando o nome da tabela como users
    
    # Criando a tabela
    id = db.Column(db.Integer, primary_key=True) # o 1º parâm. é o tipo de dado da coluna e o 2º é a primary key
    nome = db.Column(db.String(120))
    senha = db.Column(db.String(60))
    email = db.Column(db.String(120), unique=True) # o 1º parâm. é o tipo de dado da coluna e o 2º é para dizer que é único po usuário
    
    # Marcando que todos os elementos passados como parâm. serão necessários para criação do usuário na tabela
    def __init__(self, nome, senha, email):
        self.nome = nome
        self.senha = senha
        self.email = email
        
    def __repr__(self):
        return "<User %r>" % self.nome # Função para retornar o nome dos usuários existentes na tabela
