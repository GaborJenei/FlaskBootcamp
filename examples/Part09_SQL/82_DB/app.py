import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Grab the filename and the directory name
# And create an absolute path
# __file__ --> app.py
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# Setting up SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# set up a table
class Puppy(db.Model):
    # default table name can be overwritten
    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # This will be printed
    def __repr__(self):
        return f"Puppy {self.name} is {self.age} old"