from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

# Use environment variables for this later on
app.config['SECRET_KEY'] = 'my_secret_key'


# Normally this is in a separate file
class MyForm(FlaskForm):
    # Just pass on the label as string
    breed = StringField("What breed are you")
    submit = SubmitField("Submit")


@app.route('/', methods=['GET', 'POST'])
def index():
    breed = False

    # create a form object
    form = MyForm()

    if form.validate_on_submit():
        # grab the data from the form field to a variable
        breed = form.breed.data
        # set the field empty
        form.breed.data = ''

    return render_template('index.html', form=form, breed=breed)


if __name__ == '__main__':
    app.run(debug=True)
