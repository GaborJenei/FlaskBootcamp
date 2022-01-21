from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    name = 'Gabor'
    letters = list(name)
    pup_dict = {'pup_name': 'Sammy'}

    my_list = [1, 2, 3, 4, 5]

    puppies = ['Fluffy', 'Rufus', 'Spike']

    # CODE CODE
    user_logged_in = False


    # We push through the "some_variable" to the the html
    # Check the html file where it's captured (using Jinja templating)

    return render_template('basic.html', name=name, letters=letters, pup_dict=pup_dict,
                           my_list=my_list, puppies=puppies, user_logged_in=user_logged_in)


if __name__ == '__main__':
    app.run(debug=True)
