
from flask_wtf import FlaskForm
from  wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import Email,Length,DataRequired,EqualTo,ValidationError
from flaskblog.models import User

class RegistrationForm(FlaskForm):
    email=StringField('email',validators=[DataRequired(),Email()])
    username=StringField('Username' ,validators=[DataRequired(),Length(min=4,max=30)])
    password=PasswordField('password' ,validators=[DataRequired()])
    confirm_password=PasswordField('Confirm password' ,validators=[DataRequired(),EqualTo('password')])
    
    submit=SubmitField('SignUp')

    def validate_username(self,username):
        user=User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("Username already taken!")

    def validate_email(self,email):
        email=User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError("Email already taken !")

class LoginForm(FlaskForm):
    email=StringField('email',validators=[DataRequired(),Email()])
    password=PasswordField('password', validators=[DataRequired()])
    remember=BooleanField()
    submit=SubmitField('Login')