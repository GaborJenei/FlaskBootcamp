from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():

    name = 'Gabor'
    letters = list(name)
    pup_dict = {'pup_name':'Sammy'}
    # We push through the "some_variable" to the the html
    # Check the html file where it's captured (using Jinja templating)
    return render_template('basic.html', name=name, letters=letters, pup_dict=pup_dict)


if __name__ == '__main__':
    app.run(debug=True)
