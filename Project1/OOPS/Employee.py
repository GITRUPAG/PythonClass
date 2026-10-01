class Employee:  # parent class

    def __init__(self, name): # to Initialize attributes at object creation
        # self.id = id
        self.name = name
        # self.salary = salary

    def greet(self):
        print("Welcome Employee!!")

class Developer(Employee):  # child class

    def greet(self):   # Method Overriding
        super().greet()
        print("Welcome Developer!!")

    def __init__(self, name, language):
        # self.name = name
        super().__init__(name) # calling parent attribute
        self.language = language
    def display(self):
        super().greet()
        print(self.name)
        print(self.language)

d = Developer("Ravi", "Python")

d.display()

s = Employee("Ravi")

s.greet()
d.greet()

# s = Employee(101, "Ravi", 2055) # parent object







# e = Employee(101, "rupa", 20000)
# e1 = Employee(102, "alice", 5000)
# e3 = Employee(103, "Bob", 6000)
#
# e.id = 101
# e.name = "Rupa"
# e.salary = 20000
#
# e1 = Employee()
#
# e1.id = 102
#
