# app.py
import os
# from model import Pup, Owner, db
from form import AddPupForm, DelPupForm, AddOwnerForm
from flask import Flask, render_template, url_for, redirect
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = 'my_secret_key'

base_dir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'exercise.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app, db)


# Data Model
class Pup(db.Model):

    __tablename__ = 'puppies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

    # relationship
    owner = db.relationship('Owner', backref='puppy', uselist=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        # Owner
        if self.owner:
            return f"Puppy {self.name} ({self.id}) and owner {self.owner.name}"
        else:
            return f"Puppy {self.name} ({self.id})"


class Owner(db.Model):

    __tablename__ = 'owners'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

    # relationship
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self, name, puppy_id):
        self.name = name
        self.puppy_id = puppy_id


# Views

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add', methods=['GET', 'POST'])
def add_pup():

    form = AddPupForm()

    if form.validate_on_submit():

        name = form.name.data
        pup = Pup(name)
        db.session.add(pup)
        db.session.commit()

        return redirect(url_for('list_pups'))

    return render_template('pup_add.html', form=form)


@app.route('/list')
def list_pups():

    pups = Pup.query.all()

    return render_template('pup_list.html', pups=pups)


@app.route('/del', methods=['GET', 'POST'])
def del_pup():

    form = DelPupForm()

    if form.validate_on_submit():

        puppy_id = form.pup_id.data
        pup_remove = Pup.query.get(puppy_id)

        db.session.delete(pup_remove)
        db.session.commit()
        print("It should be done")

        return redirect(url_for('del_pup'))

    return render_template('pup_del.html', form=form)


@app.route('/owner_add', methods=['GET', 'POST'])
def owner_add():

    form = AddOwnerForm()

    if form.validate_on_submit():
        owner_name = form.owner_name.data
        pup_id = form.pup_id.data

        new_owner = Owner(owner_name, pup_id)

        db.session.add(new_owner)
        db.session.commit()

        return redirect(url_for('list_pups'))

    return render_template('owner_add.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
