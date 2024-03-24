class BaseClass:
    def call_me(self):
        print("Base Class Method")

class LeftSubclass(BaseClass):
    def call_me(self):
        super().call_me()
        print("Left Subclass Method")

class RightSubclass(BaseClass):
    def call_me(self):
        super().call_me()
        print("Right Subclass Method")

class Subclass(LeftSubclass, RightSubclass):
    def call_me(self):
        super().call_me()
        print("Subclass Method")

subClass = Subclass()
print(subClass.__class__.__mro__)
subClass.call_me()