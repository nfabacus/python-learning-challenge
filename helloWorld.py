my_str = 'Hello, World!'

print(my_str)

print(my_str[7])
print(my_str[:7])
print(my_str[7:])
print(my_str[4:9])
print(my_str[2:10:2])
print(my_str[::-1])

my_str_len = len('hello')
print (my_str_len)

x = "Hello, "
y = "I am learning Python!"
z = x + y
print(z)
print(z.upper())
z = z.split('i')
print(z)

print('This is a string {}, and another one is {}.'.format('INSERTED', 'Hello'))
print('The {2} {1} {0}.'.format('fox', 'brown', 'quick'))
print('The {q} {b} {f} {f}.'.format(f='fox', b='brown', q='quick'))
print('My string is {}'.format(y))
result = 100000/777
print('The resut was {r:1.3f}'.format(r=result))
name = "Tony"
print(f'Hello, his name is {name}.')

# list [,,]
my_list = [1,2,"Foo"]
print(len(my_list))
print(my_list[0])
print(my_list[2])
another_list = [3, "bar", 4]
print(my_list)
print(another_list)
total_list = my_list + another_list
print(total_list)
total_list[0] = "Hello"
total_list.append(100)  # add to the end of the array.
print(total_list)
popped_item = total_list.pop()
popped_item2 = total_list.pop(1)
print(f"popped_item is {popped_item}")
print("popped_item2 is {}".format(popped_item2))
print(total_list)

# list -  sort
new_list = [ 'x', 'a', 'j', 'c', 'f']
num_list = [4, 2, 5, 4, 9, 7]
new_list.sort()  # Important!  sort first then assign it to the new variable, otherwise it will return none.
num_list.sort()
sorted_new_list = new_list
sorted_num_list = num_list
print(sorted_new_list)
print(sorted_num_list)
new_list.reverse()
num_list.reverse()
print(sorted_new_list)
print(sorted_num_list)

# dictionaries - equivalent to javascript JSON object { : }
my_dict = {'fruit': 'banana', 'vegetable': 'carrot', 'numberArr': [1, 2, 3]}
print(my_dict['fruit'])
print(my_dict['vegetable'])
print(my_dict['numberArr'][1])
my_dict['greeting'] = 'Hello'
print(my_dict)
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

# tuples ()
my_first_tuple = (0, 1, 5, 3, 5, 5, "Hello", 8, 5)
print(my_first_tuple)
print(my_first_tuple[3])  # tuple is very similar to list but is immutable.
# tuples cannot be sorted
countOfFive = my_first_tuple.count(5)  # count how many times 5 comes up in the tuple
print('count of five: ', countOfFive)
print('indexOfHello: ', my_first_tuple.index('Hello'))

#sets {}
myset = set()
myset.add(8)
myset.add(6)
myset.add('test')
myset.add(3)
myset.add(3)
myset.add(8)

print('myset is {}'.format(myset))

my_list = [4, 9, 7, 7, 2, 2, 4, 4, 9, 7, 'ho', 'ho']
print(f'mylist is {my_list}')
my_new_set = set(my_list)
print('My new set converted from the list is {}'.format(my_new_set))

print(set('Mississippi'))

# boolean
# True, False with the first letter capitalised

# Comparision operator is almost the same as javascript, apart from ==, !=
# Chaining Comparision operators - use 'and' and 'or' and 'not'
