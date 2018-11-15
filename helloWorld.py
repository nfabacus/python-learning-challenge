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