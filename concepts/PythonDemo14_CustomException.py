# This file provides demo about exception handling
# try-except statement
# finally and else block
# raise built-in exception
# create and raise custom exception

class InvalidAgeError(ValueError):
    def __init__(self, age_):
        self.age = age_

    def __str__(self):
        return f"Given age is {self.age}. Age should be >= 18"


def validateAge(age_):
    if age < 18:
        raise InvalidAgeError(age_)
    else:
        return True


try:
    age = 17
    validateAge(age)
except InvalidAgeError as e:
    print(e)
else:
    print("Age validation successful!!")
finally:
    print("Age validation process completed.")
