students ={}

def add_student(name, marks):
    students[name] = marks # adding key value pair
    print("Student added successfully")

def update_marks(name, marks):
    if name in students: # checking name in dictionary
       students[name]= marks # updating
       print("Marks updated Successfully!!")
    else:
        print("Student not found")

def display_students():
    if len(students) == 0:
       print("No student records")
    else:
        print("\nStudent Records")
        for name, marks in students.items():
            print(name, ":", marks)

add_student("Alice", 10)
add_student("Rupa", 200)
add_student("BOB",150)
add_student("Alice", 10)

display_students()

update_marks("Alice", 50)

display_students()

# Name : "Alice"