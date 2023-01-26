from flask import render_template
from app import app
from app.models.forms import LoginForm, RegisterForm

@app.route("/index/<user>")
@app.route("/", defaults={"user":None}) # Rota padrão com um Hello World
def index(user):
    return render_template('index.html', user= user)

@app.route("/login", methods=["GET", "POST"])
@app.route("/login.html", methods=["GET", "POST"])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)
    else:
        print(form.errors)
        
    return render_template('login.html', form= form)

@app.route("/register", methods=["GET", "POST"])
@app.route("/register.html", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    
    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)
    else:
        print(form.errors)
        
    return render_template('register.html', form= form)
