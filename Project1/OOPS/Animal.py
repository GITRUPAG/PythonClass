class Animal:  # parent class

    def eat(self):
        return "Eating"
    def sleep(self):
        return "Sleeping"

class Dog(Animal): # child class
    def bark(self):
        return "Barking!!"

class Cat(Dog):
    None


d = Dog()

a = Animal()

print(d.eat())

print(d.sleep())

print(d.bark())








