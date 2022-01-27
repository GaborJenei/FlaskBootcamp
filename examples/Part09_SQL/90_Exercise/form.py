# form.py

from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField


class AddPupForm(FlaskForm):
    name = StringField('Puppy name: ')
    submit = SubmitField('Add Pup')


class DelPupForm(FlaskForm):
    pup_id = IntegerField('Pup ID to remove from the database: ')
    submit = SubmitField('Remove')


class AddOwnerForm(FlaskForm):
    owner_name = StringField('Owner Name: ')
    pup_id = IntegerField('Pup ID to adopt')
    submit = SubmitField('Adopt')