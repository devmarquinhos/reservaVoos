from flask_wtf import FlaskForm
from wtforms import fields
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = fields.StringField("username", validators=[DataRequired()])
    password = fields.PasswordField("password", validators=[DataRequired()])
    rememberMe = fields.BooleanField("remeberMe")