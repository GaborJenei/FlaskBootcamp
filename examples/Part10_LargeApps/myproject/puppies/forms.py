from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddForm(FlaskForm):
    name = StringField('Puppy name: ')
    submit = SubmitField('Add Pup')


class DelForm(FlaskForm):
    id = IntegerField('Pup ID to remove from the database: ')
    submit = SubmitField('Remove')
