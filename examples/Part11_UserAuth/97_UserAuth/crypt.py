from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

password = 'supersecretpassword'

hashed = bcrypt.generate_password_hash(password=password)

print(hashed)

check = bcrypt.check_password_hash(hashed, '$2b$12$PM/5cMRXP0OXzvhJ5IH7BO1DE5jF2KIH4NNFAOVVQqpXL/M6z4O3K')
print(check)