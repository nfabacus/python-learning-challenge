# Examples of map function
def square(num):
    return num ** 2

my_nums = [1,2,3,4,5]


for item in map(square, my_nums):
    print(item)

my_square_list = list(map(square, my_nums))
print(my_square_list)

 ## lambda expressions
print(list(map(lambda num: num**2, my_nums)))


def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'EVEN'
    else:
        return mystring[0]

names = ['Andy', 'Eve', 'Sally']

spliced_names = list(map(splicer, names))
print(spliced_names)



### Examples of filter function

def check_even(num):
    return num % 2 == 0


num_list = [1, 2, 3, 4, 5, 6]

filtered_list = filter(check_even, num_list)
print(list(filtered_list))
   ## lambda expressions
filtered_list2 = filter(lambda num: num % 2 == 0, num_list)
print(list(filtered_list2))


for n in filter(check_even, num_list):
    print(n)
