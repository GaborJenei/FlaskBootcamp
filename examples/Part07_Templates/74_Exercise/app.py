from flask import Flask, render_template, request
import re

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/report')
def report():
    # Grab the user name sent via the form
    user_name = request.args.get('user_name')

    # Do the checks
    # Capital letter
    is_upper = any([c.isupper() for c in user_name])

    # Lowercase letter
    is_lower = any([c.islower() for c in user_name])

    # Last character is number
    is_num = user_name[-1].isdigit()

    if is_upper & is_lower & is_num:
        message = "Your user name is good"
        issue_list = []
    else:
        message = "Your user name needs updating."
        issue_list = ['No capital letter', 'No lower case letter', 'No Digit']
        issue_list = [i for (i, v) in zip(issue_list, [is_upper, is_lower, is_num]) if not v]

    return render_template('report.html', user_name=user_name, message=message, issue_list=issue_list)


if __name__ == '__main__':
    app.run(debug=True)
