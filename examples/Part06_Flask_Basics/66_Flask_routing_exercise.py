from flask import Flask

app = Flask(__name__)


@app.route('/puppy_latin/<name>')
def puppy_latin(name):
    
    pup_name = ''
    
    if name.lower()[-1] == 'y':
        pup_name = name[:-1] + 'iful'
    else:
        pup_name = name + 'y'
    return "<h1>Puppy Latinator</h1><h2>your puppy latin name: {}".format(pup_name)


if __name__ == '__main__':
    app.run(debug=True)
