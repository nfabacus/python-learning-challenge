hungry = True
haveMoney = False

if hungry:
    print("I am hungry.")
    if haveMoney:
        print(""
              "Buy some food.")

elif haveMoney:
    print("Deposit")
else:
    print("Work")


my_iterable = [1,2,3]

for item in my_iterable:
    print(item)

my_tuple = ("a", "b", 15)

for item in my_tuple:
    print(item)

my_list = [(1,2), (3,4), (5,6)]
for item in my_list:
    print(item[0], item[1])
for (a, b) in my_list:
    print(a, b)

my_dictionary = { "color": "green", "height": 172, "shirt": "blue" }

for key, value in my_dictionary.items():
    print('Key is {}. Value is {}.'.format(key, value))

for value in my_dictionary.values():
    print(f'> value is {value}')

for key in my_dictionary.keys():
    print(f'> key is {key}')

for i in range(10):
    print(f'for loop i is {i}')

x = 0

while x < 20:
    if x == 5:
        print('number is 5')
        x+=1
        continue
    print('value of x is {}'.format(x))
    x += 1
    if x == 8:
        pass # just do nothing
    if x == 15:
        break
else:
    print('x is not smaller than 5')


# range
for num in range(0, 11, 2):
    print(num)

rangeToList = list(range(0, 11, 2))
print(rangeToList)

# enumerate
word = 'abcde'
for index, letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')

# zip
print('zip >>>>')
mylist1 = [1, 2, 3, 4, 5, 6]
mylist2 = ['a', 'b', 'c']
mylist3 = [100, 200, 300]

print(zip(mylist1, mylist2, mylist3))

for item in zip(mylist1, mylist2, mylist3):
    print(item)

zipToList = list(zip(mylist1, mylist2))
print(zipToList)

# Check if something is in a string or array
doesExist = 2 in [1, 2, 3]
print(doesExist)
doesExist = 'x' in [1, 2, 3]
print(doesExist)
doesExist = 'W' in 'Hello World!'
print(doesExist)
doesExist = 'myKey' in { 'myKey': 10 }
print(doesExist)
d = { 'myKey': 10 }
doesExist = 'myKey' in d.keys()
print(doesExist)
myList = [10, 20, 30, 15, 8, 100, 7]

# min/max
print(min(myList))
print(max(myList))

# random library
print('random >>>')
from random import shuffle
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shuffle(mylist)
print(mylist)

from random import randint
myInt = randint(0, 100)
print(myInt)

# input - accepts anything, and returns a string
result = input('What is your name? ')
print(f'Hello, {result}!')
result = int(input('Enter a number here ::'))
print(f'You entered >> {result}')

