class Animal():
    def __init__(self, name="animal"):
        self.name = name
        print("Animal created!")

    def who_am_i(self):
        print("I am an animal.")

    def eat(self):
        print("I am eating.")

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")

myAnimal = Animal()
myAnimal.who_am_i()
myAnimal.eat()

# Inheritance
class Dog(Animal):
    # def __init__(self, name):
    #     Animal.__init__(self, name)
    #     print("Dog created!")

    # Overriding parent class methods
    def eat(self):
        print("I am a dog eating.")

    def walk(self):
        print("I am walking.")

    def speak(self):
        return self.name + " says woof!"

    def take(self, number):
        print(f"{self.name}: It is a number: {number}.")


class Cat(Animal):
    def speak(self):
        return self.name + " says meow!"

myDog = Dog("Goofy")
myDog.who_am_i()
myDog.eat()
myDog.walk()
print(myDog.speak())
myDog.take(5)

myCat = Cat("Tom")
print(myCat.speak())


