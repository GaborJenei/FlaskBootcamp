from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField


class AddForm(FlaskForm):
    name = StringField('Owner Name: ')
    pup_id = IntegerField('Pup ID to adopt')
    submit = SubmitField('Adopt')
