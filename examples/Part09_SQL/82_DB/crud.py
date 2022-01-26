from app import db, Puppy

# Create or add a new item (row)
print('\nCreate')
my_puppy = Puppy('Rufus', 5)
db.session.add(my_puppy)
db.session.commit()

# Read
print('\nRead')
# grab all puppies
all_pups = Puppy.query.all()
print(all_pups)

# select by id
puppy_one = Puppy.query.get(1)
print(puppy_one.name)

# Filters
pup_frank = Puppy.query.filter_by(name='Frankie')
# This may return multiple rows
print(pup_frank.all())
# 'Frankie is 3 years old'

# UPDATE
print('\nUpdate')
first_puppy = Puppy.query.get(1)
first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()

first_puppy = Puppy.query.get(1)
print(first_puppy)

# Delete
print('\nDelete')
sec_pup = Puppy.query.get(2)
db.session.delete(sec_pup)
db.session.commit()

# Check the changes
print('\nChanges')
all_pups = Puppy.query.all()
print(all_pups)