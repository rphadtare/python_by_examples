# This file gives demo about different types of variables
# and there usages

print("Welcome to python demo!!!")


# local variable
def _local_variable_demo() -> None:
    print("Inside _local_variable_demo")
    x = 10
    print("Value of x ", x)
    return None


_local_variable_demo()

name = "Rohit"


# global variable
def _global_variable_demo() -> None:
    print("Inside _global_variable_demo")
    global name
    name += " Phadtare"
    print("Value of name ", name)
    return None


_global_variable_demo()


# non local variable
def _non_local_variable_demo() -> None:
    print("Inside _non_local_variable_demo")
    num = 10
    print("value of nonlocal variable before calling _inside_func ", num)

    def _inside_func() -> None:
        num1 = 20
        nonlocal num
        num += num1

    _inside_func()
    print("value of nonlocal variable post execution of _inside_func ", num)


_non_local_variable_demo()

# Object Identity demo
a = 50
b = a
print("ID of a ", id(a))
print("ID of b ", id(b))
b = 100
print("after assigning new value ")
print(f"Value of a: {a} and b: {b}")
print("ID of a ", id(a))
print("ID of b ", id(b))
