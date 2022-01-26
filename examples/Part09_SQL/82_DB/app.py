import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Grab the filename and the directory name
# And create an absolute path
# __file__ --> app.py
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# Setting up SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Connect flask migrate
Migrate(app, db)
# After this we need to set the environment variable FLASK_APP=app.py or whatever the main app python file is called
# on Win set FLASK_APP=app.py
# on Linux export FLASK_APP=app.py


# set up a table
class Puppy(db.Model):
    # default table name can be overwritten
    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    breed = db.Column(db.Text)

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    # This will be printed
    def __repr__(self):
        return f"Puppy {self.name} is {self.age} old"