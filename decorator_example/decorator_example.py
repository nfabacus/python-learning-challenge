def hello(name='Bob'):
    print('The hello function is executed.')

    def greet():
        return '\t This is the greet function inside hello!'

    def welcome():
        return '\t This is welcome function inside hello'

    if name == 'Bob':
        return greet
    else:
        return welcome

my_func = hello('Tony')
print(my_func())


def new_decorator(original_func):

    def wrap_func():
        print('Some extra code before the original function')
        original_func()
        print('Some extra code after the original function')

    return wrap_func

### decorator does the same thing as below ###
# def original_function():
#     print('I am original function.')

# wrapped_function = new_decorator(original_function)
# wrapped_function()
###############################################

@new_decorator
def original_function():
    print('I am original function.')

original_function()