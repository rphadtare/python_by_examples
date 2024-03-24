# This file gives demo about functions

def function_with_arg(arg1, arg2="Pooja"):
    print("Value of arg1 ", arg1)
    print("Value of arg2 ", arg2)
    print("*" * 25)


print("Calling function_with_arg with one parameter")
function_with_arg("Rohit")

print("Calling function_with_arg with two parameter values")
function_with_arg("Rohit", "Phadtare")

# calling function with arguments name
print("Calling function_with_arg with argument name")
function_with_arg(arg2="Rohit", arg1="Phadtare")


def function_var_arg_demo(*args):
    print("Inside function_var_arg_demo...")
    cnt = 1
    for i in args:
        print("param{} value is {} ".format(cnt, i))
        cnt += 1

    print("*" * 25)


function_var_arg_demo("Rohit", "Prakash", "Phadtare")


def function_var_karg_demo(**kargs_list):
    print("Inside function_var_karg_demo...")
    cnt = 1
    for param_name, param_value in kargs_list.items():
        print("{} value is {} ".format(param_name, param_value))
        cnt += 1

    print("*" * 25)


function_var_karg_demo(first_name="Rohit", middle_name="Prakash", last_name="Phadtare")


def lambda_func_demo(input_list):
    print("Inside lambda_func_demo .. ")
    print("Given list : ", input_list)

    list_even_num = list(filter(lambda n: (n % 2 == 0), input_list))

    print("Filtered list with even values : ", list_even_num)
    print("*" * 25)


lambda_func_demo(range(10, 21))
