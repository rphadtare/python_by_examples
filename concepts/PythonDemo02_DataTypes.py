# This file gives demo about different data types

# Numeric data type
# Int, Float, Complex data type

def _numeric_data_type_demo() -> None:
    print("Inside _numeric_data_type_demo")
    a = 10
    b = 10.5
    c = 1 + 2.3j

    print("Data type of a ", type(a), " and valud of a ", a)
    print("Data type of b ", type(b), " and valud of b ", b)
    print("Data type of c ", type(c), " and valud of c ", c)
    print("c.real ", c.real, " c.imag", c.imag)
    print("Adding 1 to c.real and adding 2 to imag part of c")
    c = c.__add__(1 + 2j)
    print("Value of c post changes ", c)
    print("**" * 25)


_numeric_data_type_demo()


# Sequence data type
# String, List, tuple type

def _string_data_type_demo() -> None:
    print("Inside _string_data_type_demo")
    _my_str = 'Hello'
    _my_str1 = " World"
    _my_str2 = """!!!"""

    # concat strings
    _final_str = _my_str + _my_str1 + _my_str2
    print("Final string ", _final_str)

    # slice operation, here string index will start from 0 and traverse till 5-1 index position i.e. 4
    print("_final_str[0:5] ", _final_str[0:5])

    # to reverse string
    print("Reverse string ", _final_str[::-1])

    # update string at specific position
    # strings are immutable hence they can modify using below way only
    _new_str = "RM"
    print("Before update char at 2nd position : ", _new_str, " and id : ", id(_new_str))
    _new_str = _new_str[0:1] + "A" + _new_str[-1]
    print("Post update char at 2nd position : ", _new_str, " and id : ", id(_new_str))

    # Repetition factor
    print("**" * 25)


_string_data_type_demo()


def _list_data_type_demo() -> None:
    print("Inside _list_data_type_demo")
    _my_list = [1, "Rohit", 2, "Pooja"]
    print("List : ", _my_list)

    # slice operation
    print("List slice [0:2] : ", _my_list[:2])

    # to reverse list
    print("Reverse list ", _my_list[::-1])

    # concat with another list
    print("Another List : ", [3, "Ram"])
    _my_list = _my_list + [3, "Ram"]
    print("Concat List : ", _my_list)

    # add element at specific position
    _my_list.insert(2, 4)
    print("Inserting element 4 at 2nd position ", _my_list)

    # removing element from specific position
    _my_list.pop(2)
    print("Removing element from 2nd position ", _my_list)

    print("**" * 25)


_list_data_type_demo()


def _tuple_data_type_demo() -> None:
    print("Inside _tuple_data_type_demo")
    _my_tuple = (1, "Rohit", 31, 25000)
    print("_my_tuple : ", _my_tuple)

    # slice
    print("Tuple slice [0:2] : ", _my_tuple[:2])

    # get element at 3rd position
    print("get element at 4th position : ", _my_tuple[3])

    # iterate through tuple
    print("Iterate through tuple")
    for i in _my_tuple:
        print(i)

    print("**" * 25)


_tuple_data_type_demo()


def _dictionary_data_type_demo() -> None:
    _my_map = {1: "Rohit", 2: "Pooja", 5: "Virat"}
    print("_my_map", _my_map)

    print("Get value of key 5 : ", _my_map[5])

    print("Get all keys : ", _my_map.keys())
    print("Get all values : ", _my_map.values())

    # check if key is present or not
    print("Check key 3 present or not : ", _my_map.__contains__(3))

    _my_map.pop(2)
    print("Post Removal of key 2 : ", _my_map)

    _my_map.update({1: "Pooja"})
    print("Post updating value of key 1 : ", _my_map)

    print("**" * 25)


_dictionary_data_type_demo()


def _set_data_type_demo() -> None:
    set1 = {1, 1, "Rohit"}
    print("set1 ", set1)
    set1.add("Pooja")
    print("set1 after adding element 'Pooja' ", set1)

    set1.add("Pooja")
    print("set1 after adding same element 'Pooja' ", set1)

    print("**" * 25)


_set_data_type_demo()


def _list_comprehension_demo():
    int_list = [10, 20, 30, 40, 11, 13, 23, 24]
    odd_number_squares_list = [n * n for n in int_list if n % 2 != 0]
    print("Input list:", int_list)
    print("Output list:", odd_number_squares_list)


_list_comprehension_demo()


