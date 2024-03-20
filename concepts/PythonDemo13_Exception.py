# This file provides demo about exception handling
# try-except statement
# finally and else block
# raise built-in exception

def demo(a, b=0):
    if b == 0:
        raise ValueError("Value of second argument should not be 0")
    else:
        c = a / b

    return c


try:
    print(demo(10))
except ZeroDivisionError:
    print("Exception handled")
except ValueError as e:
    print(e)
else:
    print("Function Demo executed successfully!!")
finally:
    print("This is finally block!!")
