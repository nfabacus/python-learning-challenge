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

# sort
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

