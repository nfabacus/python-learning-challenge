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



