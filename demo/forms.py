from flask.ext.wtf import Form
from wtforms import TextField
from wtforms.validators import Required


class AccessTokenForm(Form):
    access_token = TextField('access_token', validators = [Required()])
