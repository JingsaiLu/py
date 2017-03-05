from flask_wtf import Form
from wtforms import TextField, BooleanField, PasswordField
from wtforms.validators import Required

class LoginForm(Form):
    name = TextField('name', validators=[Required()])
    password = PasswordField('password', validators=[RuntimeError()])
    remember_me = BooleanField('remember_Me', default=False)