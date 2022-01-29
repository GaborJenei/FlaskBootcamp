from werkzeug.security import generate_password_hash, check_password_hash

hashed_p = generate_password_hash('My_password')

print(hashed_p)

check = check_password_hash(hashed_p, 'My_password')
print(check)