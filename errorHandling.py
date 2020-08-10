try:
    result = 10 + 20
    print(result)
except TypeError:
    print("TypeError!")
except:
    print("Error! You are not adding correctly")
else:
    print('Add went well')
finally:
    print('all done!')

