def my_func(arg_a, arg_b):
    return arg_a / arg_b


div1 = int(input("Input the divisible"))
div2 = int(input("Input the divider"))
if div2 == 0:
    print("0 is't possible in divider, please try again")
else:
    print("Result =", my_func(div1, div2))
