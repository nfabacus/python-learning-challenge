# one.py

def func():
    print("func() in one.py is run")

print("Top level in one.py")

if __name__ == '__main__':
    print("__name__variable is set to " + __name__)
    print('one.py is being run directly!')
    # can run code/functions in here.

else:
    print("__name__variable is set to " + __name__)
    print('one.py has been imported')