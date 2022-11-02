# Polymorphism.py
# Show the polymorphism concept using classes

# Person class, contains name and age and gender
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return "Name: " + self.name + ", Age: " + str(self.age)

    # Python doesn't really have method overloading, so the closest thing is to check for the argument's type
    def callme(self, *names):
        # Find if the argument is string or int
        if isinstance(names[0], str):
            strcall = "Hello "
            for name in names:
                strcall += name + ", "
            strcall += "my name is " + self.name
            print(strcall)
        elif isinstance(names[0], int):
            print("Hello, my name is " + self.name + ", the sum of the numbers is " + str(sum(names)))


# Student class, inherits from Person class
class Student(Person):
    def __init__(self, name, age, gender, student_id):
        Person.__init__(self, name, age, gender)
        self.student_id = student_id

    # Override the str method
    def __str__(self):
        return Person.__str__(self) + ", Student ID: " + str(self.student_id)


# Teacher class, inherits from Person class
class Teacher(Person):
    def __init__(self, name, age, gender, teacher_id):
        Person.__init__(self, name, age, gender)
        self.teacher_id = teacher_id

    # Override the str method
    def __str__(self):
        return Person.__str__(self) + ", Teacher ID: " + str(self.teacher_id)


# Main function
def main():
    # Create a student object
    student1 = Student("John", 18, 1, 60122000)
    student2 = Student("Mary", 19, 0, 60122001)
    # Create a teacher object
    teacher1 = Teacher("Jack", 30, 1, 45679617)
    teacher2 = Teacher("Jane", 29, 0, 45679618)
    # Create a list of Person objects
    person_list = [student1, student2, teacher1, teacher2]
    # Print the information of each person
    person1 = Person("David", 20, 1)
    person1.callme("David", "John", "Mary")
    person1.callme(1, 2, 3, 4, 5)

    for person in person_list:
        # The polymorphism concept is used here to print the information of each person
        # It calls the correct __str__ method of each class thanks to the overrides we made in the classes
        print(person)


# Call the main function
main()