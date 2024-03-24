# This file gives demo about multilevel inheritance

class Animal:

    animal_id = 0
    def __init__(self, name, id):
        print("This is animal...")
        self.__name = name
        self.animal_id = id

    def speak(self):
        print("Animal {} with id {} speaks ..."
              .format(self.__name, self.animal_id))


class Dog(Animal):

    def __init__(self, name, id_):
        super().__init__("Dog", id_)
        print("This is Dog..")
        self.__name = name

    def speak(self):
        print("Dog with name '{}' and with id {} barks ..."
              .format(self.__name, self.animal_id))


d = Dog("Tobo", 1)
d.speak()
print(d.__dict__)
