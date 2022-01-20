from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello Puppy!</h1><h2>Hello Gabe</h2>'


if __name__ == '__main__':
    app.run()
