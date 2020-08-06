# two.py

import one

print("Top leve in two.py")

one.func()

if __name__ == '__main__':
    print("__name__variable is set to " + __name__)
    print("two.py is being run directly")
    # can run code/functions in here.

else:
    print("__name__variable is set to " + __name__)
    print("two.py is being imported")
