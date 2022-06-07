def my_f(*args):
    try:
        t = [*args][0].split()
        result = [int(item) for item in t]
#        t1 = sum(t)
        return sum(result)
    except TypeError:
        return 'Error'


num = []
Flag = True
summ = 0
while Flag:
    i1 = 0
    num = input('Input a number with ' ', for stop enter Q, please')
    for i in num:
        if i == "Q" and i1 != 0:
            Flag = False
            print("Good buy")
            m = num[:i1] + '0'
            summ = my_f(m)
            print("Sum result is: ", summ)
        elif i == "Q" and i1 == 0:
            Flag = False
            print("Good buy")
            break
        i1 += 1
    if Flag:
        summ += my_f(num)
        print("Sum result is: ",summ)
