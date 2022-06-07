def my_func(x, y):
    try:
        count = y * (-1)
        div = x
        while count > 1:
            div *= x
            count -= 1
        res = 1 / div
        return res

    except TypeError:
        return 'Error'


num1 = float(input("Input a number"))
num2 = int(input("Input a number < 0"))
print(my_func(num1,num2))