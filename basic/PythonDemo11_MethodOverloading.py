from multipledispatch import dispatch


@dispatch(int, int)
def add_numbers(a, b):
    print("First add_numbers..")
    return a + b


@dispatch(int, int, int)
def add_numbers(a, b, c=0):
    print("Second add_numbers..")
    return a + b + c


print("Addition of two numbers 10 and 20 : ", add_numbers(10, 20))
print("Addition of two numbers 10, 20 and 30 : ", add_numbers(10, 20, 30))
