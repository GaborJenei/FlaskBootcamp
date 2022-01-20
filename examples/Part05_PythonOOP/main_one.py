# main_one.py
def func():
    print('Func in main_one.py')


print('top level in main_one.py')

if __name__ == '__main__':
    print("one.py is being run directly")
else:
    print("one.py is running imported")
