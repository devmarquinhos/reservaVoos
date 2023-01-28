from app import db # Importando o banco de dados, do __init__ na pasta-mãe app

class User(db.Model): # Criando a tabela de users usando uma padrão do Flask
    __tablename__ = "users" # Setando o nome da tabela como users
    
    # Criando a tabela
    id = db.Column(db.Integer,primary_key=True) # o 1º parâm. é o tipo de dado da coluna e o 2º é a primary key
    systemInfluence = db.Column(db.Integer)
    nome = db.Column(db.String(120))
    senha = db.Column(db.String(60))
    email = db.Column(db.String(120), unique=True) # o 1º parâm. é o tipo de dado da coluna e o 2º é para dizer que é único por usuáriodb
    
    # Marcando que todos os elementos passados como parâm. serão necessários para criação do usuário na tabela
    def __init__(self, systemInfluence, nome, senha, email):
        self.systemInfluence = systemInfluence
        self.nome = nome
        self.senha = senha
        self.email = email
        
    def __repr__(self):
        return "<User %r>" % self.nome # Função para retornar o nome dos usuários existentes na tabela

class Flight(db.Model):
    __tablename__ = "flights" # Setando o nome da tabela como flights
    
    # Criando a tabela com as colunas sobre a reserva
    flightNumber = db.Column(db.Integer, primary_key=True)
    departureAirport = db.Column(db.String(12), unique=True) # o 1º parâm. é o tipo de dado da coluna e o 2º é para dizer que é único por reserva
    arrivalAirport = db.Column(db.String(12), unique=True) # o 1º parâm. é o tipo de dado da coluna e o 2º é para dizer que é único por reserva
    flightDate = db.Column(db.String(10))
    aircraft = db.Column(db.String(12))
    pax_available = db.Column(db.Integer)
    pax_booked = db.Column(db.Integer)
    
    # Marcando quais elementos passados como parâm. são obrigatórios
    def __init__(self, flightNumber, departureAirport, arrivalAirport, flightDate, aircraft, pax_available, pax_booked):
        self.flightNumber = flightNumber
        self.departureAirport = departureAirport
        self.arrivalAirport = arrivalAirport
        self.flightDate = flightDate
        self.aircraft = aircraft
        self.pax_available = pax_available
        self.pax_booked = pax_booked
    
    def __repr__(self):
        return "<Flight %r>" % self.flightNumber # Pegando a PK dos voos