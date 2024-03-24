class Person:

    def __init__(self, name_="", id_=0):
        self.name = name_
        self.id = id_

    def __str__(self):
        return "Person [ name = {} , id = {} ]".format(self.name, self.id)

    def show(self):
        print(self)
        print("*"*50)


class Student(Person):
    def __init__(self, name_="", id_=0, std_=""):
        super().__init__(name_, id_)
        self.std = std_

    def __str__(self):
        return "Student [ name = {} , id = {}, std = {} ]".format(self.name, self.id, self.std)

    def show(self):
        print(self)
        print("*"*50)


class Employee(Person):
    def __init__(self, name_="", id_=0, salary=0):
        super().__init__(name_, id_)
        self.salary = salary

    def __str__(self):
        return "Employee [ name = {} , id = {}, salary = {} ]".format(self.name, self.id, self.salary)

    def show(self):
        print(self)
        print("*"*50)


p = Person("Rohit", 1)
s = Student("Rohit", 1, "12th")
e = Employee("Rohit", 1, 2000)

for x in (p, s, e):
    x.show()

