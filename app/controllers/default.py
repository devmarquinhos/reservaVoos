from flask import render_template
from app import app, db
from app.models.forms import LoginForm, RegisterForm
from app.models.tables import User

@app.route("/index/<user>")
@app.route("/", defaults={"user":None}) # Rota padrão com um Hello World
def index(user):
    return render_template('index.html', user= user)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)
        print(form.rememberMe.data)
    else:
        print(form.errors)
        
    return render_template('login.html', form= form)

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    
    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)
    else:
        print(form.errors)
        
    return render_template('register.html', form= form)


@app.route("/teste/<info>")
@app.route("/teste", defaults={"info": None})
def teste(info):
    i = User("1", "Julia Rizza", "1234", "juliarizza@email.com")
    db.session.add(i)
    db.session.commit()
    return "Ok"