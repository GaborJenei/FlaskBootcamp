from flask import Flask, render_template
import os


app = Flask(__name__)


# https://firebasestorage.googleapis.com/v0/b/wedding-pics-83add.appspot.com/o/1003%20B24I7821.JPG?token=6d7b3677-2818-445d-9f20-0dffb2a80e8c
# gs://wedding-pics-83add.appspot.com/1003 B24I7821.JPG?token=6d7b3677-2818-445d-9f20-0dffb2a80e8c

# Read up file names
file_names = []
root = 'gs://wedding-pics-83add.appspot.com/'
for file in os.listdir('./static'):
    file_names.append(file)


@app.route('/')
def index():
    return render_template('basic.html', pics = sorted(file_names))


if __name__ == '__main__':
    app.run(debug=True)