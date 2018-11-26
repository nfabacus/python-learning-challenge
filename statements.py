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
