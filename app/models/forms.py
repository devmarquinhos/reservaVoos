from flask_wtf import FlaskForm
from wtforms import fields
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = fields.StringField("username", validators=[DataRequired()])
    password = fields.PasswordField("password", validators=[DataRequired()])
    rememberMe = fields.BooleanField("rememberMe")

class RegisterForm(FlaskForm):
    username = fields.StringField("username", validators=[DataRequired()])
    password = fields.StringField("password", validators=[DataRequired()])
    confirm = fields.BooleanField("confirm", validators=[DataRequired()])
    
class RegisterFlight(FlaskForm):
    flightNumber = fields.IntegerField("flightNumber", validators=[DataRequired()])
    departureAirport = fields.StringField("departureAirport", validators=[DataRequired()])
    arrivalAirport = fields.StringField("arrivalAirport", validators=[DataRequired()])
    flightDate = fields.DateField("flightDate", validators=[DataRequired()])
    aircraft = fields.StringField("aircraft", validators=[DataRequired()])
    pax_available = fields.IntegerField("pax_available", validators=[DataRequired()])
    pax_booked = fields.IntegerField("pax_booked", validators=[DataRequired()])