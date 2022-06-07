def my_func(a, b, c):
    try:
        res = [a, b, c]
        s = sum(res)
        m = min(res)
        return s - m
    except TypeError:
        return 'Error'


a = int(input("Inmput number_1"))
b = int(input("Inmput number_1"))
c = int(input("Inmput number_1"))
print(my_func(a, b, c))
