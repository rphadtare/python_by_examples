# This file gives demo about multilevel inheritance


class Company:
    def __init__(self):
        print("This is Company ..")

    def show(self):
        print("We manufactures vehicles ..")


class BikeCompany(Company):

    def __init__(self):
        super().__init__()
        print("This is BikeCompany ..")

    def show(self):
        super().show()
        print("We manufactures bikes ..")


class CarCompany(Company):

    def __init__(self):
        super().__init__()
        print("This is CarCompany ..")

    def show(self):
        super().show()
        print("We manufactures cars ..")


class BusCompany(Company):

    def __init__(self):
        super().__init__()
        print("This is BusCompany ..")

    def show(self):
        super().show()
        print("We manufactures buses ..")


class Honda(BusCompany, CarCompany, BikeCompany):

    def __init__(self):
        super().__init__()
        print("This is Honda company ..")

    def show(self):
        super().show()
        print("We are Honda company")


h1 = Honda()
h1.show()

print(h1.__class__.__mro__)







