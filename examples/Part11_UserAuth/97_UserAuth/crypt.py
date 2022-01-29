from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

password = 'supersecretpassword'

hashed = bcrypt.generate_password_hash(password=password)

print(hashed)

