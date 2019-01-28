# Special (Magic/Dunder) Methods
mylist = [1,2,3]
print(len(mylist))

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):  ## upon str, do something here.
        return f"{self.title} by {self.author}, {self.pages} pages"

    def __len__(self):  ## upon len, do something here.
        return self.pages

    def __del__(self):  ## upon del, can do something here.
        print('A book object has been deleted')

# __str__ can return the string representation for the class
b = Book('Python 101', 'Bob', 200);
print(b)
print(len(b))

# How to delete variable or the instance of a class
del b

## variable b is now deleted.
print(b)

