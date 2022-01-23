from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField, RadioField,
                     SelectField, TextAreaField, SubmitField)

from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey'


class InfoForm(FlaskForm):

    breed = StringField('What breed are you?', validators=[DataRequired()])
    neutered = BooleanField("Have you been neutered")
    mood = RadioField('Please choose your mood:',
                      # list of tuple pairs
                      # first item is value code, second is what the user sees
                      choices=[('mood_1', 'Happy'), ('mood_two', 'Excited')])
    food_choice = SelectField(u'Pick your favourite food:',
                              choices=[('chi', 'Chicken') , ('bf', 'Beef'), ('fish', 'Fish')])

    feedback = TextAreaField()
    submit = SubmitField('Submit this')


@app.route('/', method=['GET','POST'])
def index():

    form = InfoForm()

    # This if statement only gets executed after clicking submit
    if form.validate_on_submit():
        # we'll get and pass the data
        session['breed'] = form.breed.data  # we'll get the internal data
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data
        session['food'] = form.food_choice.data
        session['feedback'] = form.feedback.data

        return redirect(url_for('thankyou'))

    return render_template('index.html', form=form)


@app.route('/thankyou', method=['GET'])
def thankyou():
    render_template('thankyou.html')


if __name__ == '__main__':
    app.run(debug=True)
