class Student:

    College = "SV" # Class Variables

    def __init__(self, name, age):  #Instance Variables
        self.name = name
        self.age = age
    def greet(self): # Method
        str = "hello"
        return "GM!!!"
    def display(self):
        print(self.name)
        print(self.age)

s1 = Student("Rupa", 30) # object

s1.display()
print(s1.College)


s20= Student("Ajay", 25)

s20.display()
s1.display()

print(s1.College)

print(s20.name)
print(s20.age)

s1.name = "Alice"   # Attributes
s1.age = 25

# s2 = Student()
# s2.name = "Bob"
# s3 = Student()
# s3.name = "Ajay"

print(s1.name)

