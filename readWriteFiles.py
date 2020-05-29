# I/O with Basic Files
## reading for a file
myfile = open('helloWorld.txt')
print(myfile.read())
myfile.seek(0) # you need to reset the cursor to position 0 to read the same file again.
print(myfile.readlines())
myfile.close() # important to close the file at the end.

with open('helloWorld.txt') as my_new_file:  # this way, you do not have to worry about closing the file.
    contents = my_new_file.read()

print('printing contents .... \n', contents)

## writing to a file
with open('secondFile.txt', mode='w+') as f:
    # mode can be r w a - a for append.
    # r+ for reading and writing
    # w+ for writing and reading - OVERWRITES or create a new file!
    f.write('YO! This is a new file content! \nSecond line')

with open('secondFile.txt', mode='r') as f:
    anotherContents = f.read()
    print(anotherContents)

with open('thirdFile.txt', mode='w') as f3:
    # mode can be r w a - a for append.
    # r+ for reading and writing
    # w+ for writing and reading - OVERWRITES or create a new file!
    f3.write('YO! This is a third file content!')

with open('thirdFile.txt', mode='r') as f3:
    # mode can be r w a - a for append.
    # r+ for reading and writing
    # w+ for writing and reading - OVERWRITES or create a new file!
    anotherContents = f3.read()
    print(anotherContents)

with open('thirdFile.txt', mode='a') as f3:
    # mode can be r w a - a for append.
    # r+ for reading and writing
    # w+ for writing and reading - OVERWRITES or create a new file!
    f3.write('\nThis is an additional comment!')