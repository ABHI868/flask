
from flask_wtf import FlaskForm
from  wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import Email,Length,DataRequired,EqualTo

class RegistrationForm(FlaskForm):
    email=StringField('email',validators=[DataRequired(),Email()])
    username=StringField('Username' ,validators=[DataRequired(),Length(min=4,max=30)])
    password=PasswordField('password' ,validators=[DataRequired()])
    confirm_password=PasswordField('Confirm password' ,validators=[DataRequired(),EqualTo('password')])
    
    submit=SubmitField('SignUp')

class LoginForm(FlaskForm):
    email=StringField('email',validators=[DataRequired(),Email()])
    password=PasswordField('password', validators=[DataRequired()])
    remember=BooleanField()
    submit=SubmitField('Login')