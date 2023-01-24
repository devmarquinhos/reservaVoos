from flask import render_template
from app import app
from app.models.forms import LoginForm

@app.route("/index/<user>")
@app.route("/", defaults={"user":None}) # Rota padrão com um Hello World
def index(user):
    return render_template('index.html', user= user)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('loginPage.html', form= form)
