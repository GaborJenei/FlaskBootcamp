from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello Puppy</h1>'


@app.route('/information')
def info():
    return '<h2>Puppies are cute</h2>'


# This is a dynamic route
@app.route('/puppy/<name>')
def puppy(name):
    return "<h1>100th letter: {}.</h1>".format(name[100])


if __name__ == '__main__':
    app.run(debug=True)
