from models import db, Puppy, Owner, Toy

# Create puppies
rufus = Puppy('Rufus')
fido = Puppy('Fido')

# add the puppies to the database
db.session.add_all([rufus, fido])
db.session.commit()

# Check
print('Puppies added:')
print(Puppy.query.all())

# Grab rufus
# the filter_by actually gives us back multiple items
rufus = Puppy.query.filter_by(name='Rufus').first()
print('\nCheck Rufus again:')
print(rufus)

# Create an owner fpr Rufus
jose = Owner('Jose', rufus.id)

# Give rufus some toys

toy1 = Toy('Chew toy', rufus.id)
toy2 = Toy('Ball', rufus.id)

# Commit owner
db.session.add_all([jose, toy1, toy2])
db.session.commit()

# grab rufus
rufus = Puppy.query.filter_by(name='Rufus').first()
print('\nCheck Rufus again:')
print(rufus)

rufus.report_toys()
