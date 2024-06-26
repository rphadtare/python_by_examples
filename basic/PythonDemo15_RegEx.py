# This file provides demo about regular expressions

import re


def simpleSearch():
    # create re object using compile method
    pattern = "demo"
    input_str = "Hello, This is Hello demo!!"

    print(f"Input: {input_str}")
    print(f"Search Pattern: {pattern}")

    pattern_obj = re.compile(pattern)
    match_obj = pattern_obj.search(input_str)
    print("Is pattern matched in input string: ", bool(match_obj))
    if bool(match_obj):
        print("Overall result", match_obj)
        print("Starting position of matched pattern: ", match_obj.start())
        print("End position of matched pattern: ", match_obj.end())
        print("Group : ", match_obj.group())


def matchDemo():
    pattern = "This"
    input_str = "Hello, This is regex demo !!"
    print("Result: ", re.match(pattern, input_str))


def fullMatchDemo():
    pattern = "[a-zA-Z0-9]*@{1}[a-z]{1,5}\\.[a-z]{1,3}"
    input_str = "rohitphadtare39@gmail.com"
    print("Result: ", re.fullmatch(pattern, input_str))


def findAllDemo():
    pattern = "[pP]{1}[a-z]*"
    input_str = "Pooja Rohit phadtare"
    print("Result: ", re.findall(pattern, input_str))


def findItrDemo():
    pattern = "[pP]{1}[a-z]*"
    input_str = "Pooja Rohit Phadtare"
    print("Result: ")
    cnt = 1
    for i in re.finditer(pattern, input_str):
        print(f"{cnt} match occur in input:{input_str} "
              f"at position "
              f"{i.start()} and group is {i.group()}")
        cnt += 1


def splitDemo():
    pattern = " "
    input_str = "This is split demo"
    obj = re.compile(pattern)
    print("Split result with no max splits : ")
    print(obj.split(input_str))

    print("Split result with no 1 splits : ")
    print(obj.split(input_str, 1))


def subDemo():
    pattern = "split"
    input_str = "This is split demo !!"
    obj = re.compile(pattern)
    print(f"Input string: {input_str}")
    print(f"Output string: {obj.sub('substitute', input_str)}")


def subN_Demo():
    pattern = "Java"
    input_str = "This is Java REG EX demo!! Java is OOP language"
    obj = re.compile(pattern)
    print(f"Input string: {input_str}")
    output = obj.subn('python', input_str)
    print(f"Output: {output}")
    print(f"Output string: {output[0]}")
    print(f"Number of replaced instances: {output[1]}")


def escapeDemo():
    pattern = "[RA01.*@TST"
    input_str = "[RA01.*@TST"
    pattern_with_escape = re.escape(pattern)
    print(f"Input: {input_str}")
    print(f"patten: {pattern}")
    print(f"escape patten: {pattern_with_escape}")
    print("Result: ", re.search(pattern_with_escape, input_str))


def auto_complete():
    words = ["Pinterest", "Pandora", "pile", "Pg&e"]
    input = "P"
    print(f"input - {input}")

    result_list = []
    for i in words:
        result = bool(re.search(input.lower(), i.lower()))
        print("Input", i, result)
        if result:
            result_list.append(i)

    result_list.sort(reverse=False)
    return result_list[:3]


def main():
    option = 9
    if option == 1:
        simpleSearch()
    elif option == 2:
        matchDemo()
    elif option == 3:
        fullMatchDemo()
    elif option == 4:
        findAllDemo()
    elif option == 5:
        findItrDemo()
    elif option == 6:
        splitDemo()
    elif option == 7:
        subDemo()
    elif option == 8:
        subN_Demo()
    elif option == 9:
        escapeDemo()
    elif option == 10:
        result = auto_complete()
        print(", and ".join([",".join(result[:-1]), result[-1]]))


if __name__ == "__main__":
    main()
