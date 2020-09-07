### Below first way creates a list of all items first.
# def create_cubes(n):
#     result = []
#     for x in range(n):
#         print(x)
#         result.append(x**2)
#     return result
#
# print(create_cubes(10))

### Below way does not create a list of all items, but memorises each item as it goes along.
def create_cubes(n):
    for x in range(n):
        yield x**2

for x in create_cubes(10):
    print(x)


print(list(create_cubes(10)))

my_generator = create_cubes(10)
# you can use next to get the item one by ones
print(next(my_generator))
print(next(my_generator))



# def gen_fibonacci(n):
#     a = 1
#     b = 1
#     output = []
#     for i in range(n):
#         output.append(a)
#         a, b = b, a + b
#     return output

def gen_fibonacci(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


for numb in gen_fibonacci(10):
    print(numb)


# next
def simple_gen():
    for x in range(5):
        yield x

for number in simple_gen():
    print(number)

g = simple_gen()

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
# print(next(g))  # error out when no more

s = 'hello, World!'
for letter in s:
    print(letter)

# string is iterable but not an iterator.
# next(s) # this will error.

print('###########')

# to convert string to iterator, use 'iter'
s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))


