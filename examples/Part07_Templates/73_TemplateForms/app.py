from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup_form')
def signup_form():
    return render_template('signup.html')


@app.route('/thank_you')
def thank_you():
    # Grabbing the data from the form
    # grab first name where in the html name="first_name"
    first_name = request.args.get('first_name')

    # grab last name where in the html name="last_name"
    last_name = request.args.get('last_name')

    return render_template('thankyou.html', first_name=first_name, last_name=last_name)


# This is for page not found
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)