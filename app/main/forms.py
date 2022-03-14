from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField, TextAreaField, SelectField
from wtforms.validators import InputRequired,Email,EqualTo
from ..models import Users

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about yourself:',validators = [InputRequired()])
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    category = SelectField('Category', choices=[('PickUp lines','PickUp Lines'),('Interviews','Interviews'),('Product Sale','Product Sale'),('Promotion','Promotion')],validators=[InputRequired()])
    post = TextAreaField('Your Pitch', validators=[InputRequired()])
    submit = SubmitField('Pitch')

class CommentForm(FlaskForm):
    comment = TextAreaField('Leave a comment',validators=[InputRequired()])
    submit = SubmitField('Comment')