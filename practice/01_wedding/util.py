import os

for file in os.listdir('./static'):
    print(file.replace(' ', '%'))