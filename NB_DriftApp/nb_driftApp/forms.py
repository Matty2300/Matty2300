from email.policy import default
from typing import Optional
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField
from flask_ckeditor import CKEditorField
from wtforms.validators import Email, DataRequired, EqualTo, Optional
from nb_driftApp.models import User



class loginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    
    submit = SubmitField('Log in')
    
class registerForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    fornavn = StringField('Fornavn', validators=[DataRequired()])
    efternavn = StringField('Efternavn', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    
    submit = SubmitField('Add user')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValueError('That email already exist, choose another one')
        
class postForm(FlaskForm):
    headline = StringField('Headline', validators=[DataRequired()])
    msg_content = CKEditorField('Write message', validators=[DataRequired()])
    expiration_date = DateField('Set expiration date', validators=[Optional()])
    
    submit = SubmitField('Submit')
    
 