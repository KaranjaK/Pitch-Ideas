from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField, TextAreaField
from wtforms.validators import InputRequired,Email,EqualTo
from ..models import Users

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [InputRequired()])
    submit = SubmitField('Submit')