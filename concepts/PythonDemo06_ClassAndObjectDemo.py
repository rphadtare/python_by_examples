# This file gives demo about class and object

# Class Person
class Person:
    def __init__(self, pid, name=None, age=None, gender=None):
        """constructor for person class"""
        self.pid = pid
        self.name = name
        self.age = age
        self._gender = gender

    def display_person_details(self):
        print("Person details are -")
        print("ID: ", self.pid, " Name: ", self.name, " Age : ",
              self.age, " Gender : ", self._gender)
        print("*" * 100)


# Creating Object
p1 = Person(1, "Rohit Phadtare", 31, 'M')
p2 = Person(2)

p1.display_person_details()
p2.display_person_details()


class Shape:

    def __init__(self, name_of_shape):
        self._name = name_of_shape

    def __str__(self):
        return "Shape is " + self._name


my_shape = Shape("Circle")
print(my_shape)

for _ in range(100):
    print(_)
