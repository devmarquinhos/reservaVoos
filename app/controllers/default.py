from flask import render_template
from app import app

@app.route("/index/<user>")
@app.route("/", defaults={"user":None}) # Rota padrão com um Hello World
def index(user):
    return render_template('index.html', user=user)
