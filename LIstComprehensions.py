# List Comprehensions
mystring = 'Hello'
mylist = []
for letter in mystring:
    mylist.append(letter)
print(mylist)

# for x in range(0,10):  ## print out 0 to 9.  This will exist at 10 and does not print 10.
#     print(x)

# more concise way below - comprehension
print('<<<<<<< List comprehension >>>>>>>>>>>>')
mylist2 = [letter for letter in mystring]
print(mylist2)

mylist = [x for x in 'world!']
print(mylist)

mylist = [x for x in range(0, 10)]
print(mylist)
mylist = [x**2 for x in range(0, 10)]
print(mylist)

mylist = [x**2 for x in range(0, 10) if x%2 == 0]
print(mylist)

celcius = [0, 10, 15, 20, 25, 30, 35, 40]
fahrenheit = [((9/5)*temp + 35) for temp in celcius]
print(fahrenheit)

results = [x if x%2 ==0 else 'ODD' for x in range(0, 11)]
print(results)

mylist = []

print('nested loop >>>>')
for x in [2, 4, 6]:
    for y in [1, 10, 100]:
        mylist.append(x*y)

print(mylist)
