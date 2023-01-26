from app import app
from flask_wtf.csrf import CSRFProtect, generate_csrf

csrf = CSRFProtect(app)
csrf.init_app(app)
csrfKey = generate_csrf(secret_key=app.config.from_object('config'))

if __name__ == "__main__":
    app.run()
