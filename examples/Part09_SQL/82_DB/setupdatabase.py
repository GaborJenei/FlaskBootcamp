from app import db, Puppy

# create all the tables
db.create_all()

# We can create new entries now

sam = Puppy('Sammy', 3)
frank = Puppy('Frankie', 4)

# None
# None
print(sam.id)
print(frank.id)

# add all item from the list
db.session.add_all([sam, frank])
db.session.commit()
# alternatively add one: db.session.add(sam)

print(sam.id)
print(frank.id)
