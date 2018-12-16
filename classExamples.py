class Dog():

    # class object attribute
    # same for any instance of a class
    species = 'mammal'

    def __init__(self, breed, name, spots):
        # user defined Attributes  << argument
        self.breed = breed
        self.name = name
        self.spots = spots

    # Operations/actions ----> methods
    def bark(self, number):
        for i in range(number):
            print('Woof! My name is {} {}.'.format(self.name, i))


my_dog = Dog(breed="Lab", name="Bob", spots=False)
print(my_dog.species)
print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)
my_dog.bark(10)

class Circle():
    # Class Object Attribute
    pi = 3.14

    def __init__(self, radius =1):
        self.radius = radius
        self.area = radius * radius * Circle.pi

    # Method
    def get_circumference(self):
        return self.radius * self.pi * 2


my_circle = Circle(radius=10)
print(my_circle.get_circumference())
print(my_circle.area)

