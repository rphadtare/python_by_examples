# This file gives demo about different keywords

# how to list python keywords
# option 1 - using help functions

help("keywords")

# option 2 - using keyword library
import keyword

# displaying the complete list using "kwlist()."
print("The set of keywords in this version is: ")
print(keyword.kwlist)

# Floor division and division operator difference
a, b = 11, 5
print(a // b)
print(a / b)


# switch case equivalent in python
def switch_example(value):
    match value:
        case 1:
            return "One"
        case 2:
            return "Two"
        case 3:
            return "Three"
        case _:
            return "Default case"


print(switch_example(2))


def switch_example_with_dictionary(value):
    return {
        1: "One",
        2: "Two",
        3: "Three"
    }.get(value, "Default case")


print(switch_example_with_dictionary(4))

# access list using for with index position
l1 = [1, 2, 3, 4]
for i in range(0, len(l1)):
    print(l1[i])
    if i == 1:
        print("Changing iterable variable value ..")
        i = 3

# access list using while with trying to modify iterable variable
i = 0
while i < len(l1):
    print(l1[i])
    if i == 1:
        print("Changing iterable variable value ..")
        i += 2
    else:
        i += 1

