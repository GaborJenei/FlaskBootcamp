# Data Model
from myproject import db
# Set up db in the __init__ within myproject

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
