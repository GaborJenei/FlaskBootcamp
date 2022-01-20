import main_one

print("Top level in two.py")

main_one.func()

if __name__ == '__main__':
    print('Two is being run directly')
else:
    print("Two is being imported")