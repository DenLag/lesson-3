def int_func(str):
    return str.capitalize()


str = input("Enter a word: ")
str = str.split(" ")
for i in str:
    print(int_func(i) + " ",end="")
