from app import app

@app.route("/") # Rota padrão com um Hello World
def index():
    return "Hello World!"