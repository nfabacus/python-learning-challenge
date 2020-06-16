# functions - def name_of_function():

def hello_world():
    print("Hello, World!")

hello_world()

def hello_person(name='somebody'):  # can have a default parameter
    print("Hello, " + name)

hello_person("Tony")
hello_person()

def add(a, b):
    '''
    DOCSTRING: This is to add two numbers
    input: two numbers
    output: returns addition result
    '''
    return a + b

help(add)
answer = add(2, 3)
print(answer)

def dog_check(mystring):
    return 'dog' in mystring.lower()

result = dog_check('Dog ran away')
print(result)
result = dog_check('dog ran away')
print(result)
result = dog_check('cat ran away')
print(result)