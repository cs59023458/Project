from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2,max=20)])
    email = StringField('Email', vlidators=[DataRequired(), Email()])
    password = PasswordField('Password', vlidators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', vlidators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', vlidators=[DataRequired(), Email()])
    password = PasswordField('Password', vlidators=[DataRequired()])
    remeber = BooleanField('Remeber Me')
    submit = SubmitField('Login')