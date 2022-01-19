# Decorators add some extra functionality to an already existing function

def hello(name='Gabe'):
    print('the hello() function has been run')

    def greet():
        return "     This is inside greet()"

    def welcome():
        return "     This is inside welcome()"

    # print(greet())
    # print(welcome())

    if name == 'Gabe':
        return greet
    else:
        return welcome


x = hello(name='Sam')
print(x())


def hello():
    return 'Hi Gabe!'


def other(func):
    print("Some other code")
    # Assume that func passed in is a function
    print(func())


other(hello)
print('\n\n')


def new_decorator(func):
    def wrap_func():
        print('some code before executing func')

        func()

        print('executing something else')

    return wrap_func


def func_needs_decorator():
    print("please decorate me!!!")


func_needs_decorator = new_decorator(func_needs_decorator)
func_needs_decorator()


# Equivalent
def new_decorator(func):
    def wrap_func():
        print('some code before executing func')

        func()

        print('executing something else')

    return wrap_func


def func_needs_decorator():
    print("please decorate me!!!")


@new_decorator
def func_needs_decorator():
    print("please decorate me!!!")


func_needs_decorator()
