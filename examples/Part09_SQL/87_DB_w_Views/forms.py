# Definition of forms

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):

    name = StringField('Name of Puppy:')
    submit = SubmitField('Add puppy')


class DelForm(FlaskForm):

    id = IntegerField("Id number of puppy to be deleted: ")
    submit = SubmitField("Remove puppy")

