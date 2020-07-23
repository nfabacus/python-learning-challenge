# #### *args and **kwargs #### #
def myfunc(a, b):
    return sum((a, b)) * 0.05


result = myfunc(40, 60)
print(result)


def myfunc2(*args):
    # *args will treat the arguments as a tuple. and can take any number of arguments.
    # e.g. (40. 60, 100, 1, 27)
    print(args)
    return sum(args) * 0.05

result2 = myfunc2(20, 30, 40, 110)
print(result2)


def my_kwargs_func(**kwargs):
    # kwargs - keyword args **kwargs make arguments into dictionary
    print(kwargs)
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here.')


my_kwargs_func(fruit="apple", veggie='carrot')


def my_combined_func(*args, **kwargs):
    print(args)
    print(kwargs)
    print('I like {} {}.'.format(args[2], kwargs['food']))


my_combined_func(2,3, 20, food='eggs', animal='dog')

