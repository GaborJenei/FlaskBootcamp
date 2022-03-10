from flask import Flask, render_template
import os


app = Flask(__name__)


# Read up file names
file_names = []
root = 'link to bucket'

for file in os.listdir('./static'):
    file_names.append(root + file.replace(' ', '%20'))


@app.route('/')
def index():
    return render_template('basic.html', pics = sorted(file_names))


if __name__ == '__main__':
    app.run(debug=True)