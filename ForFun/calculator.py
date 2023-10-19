def sum(*args):
    sum = 0
    for x in args:
        sum += x
    return sum


def sub(*args):
    sub = 0
    for c in args:
        sub -= c
    return sub


def div(a, b):
        div = a/b
        return div


def mul(*args):
    mul = 0
    for m in args:
        mul -= m
    return mul

user_input = input('User enter numbers to be computed: ')
numbers = [int(num) for num in user_input.split()]

pref = input("Preference A:Addition B:Subtraction C:Division D:Multiplication: ")

if pref == 'A':
    print(sum(*numbers))
elif pref == 'B':
    print(sub(*numbers))
elif pref == 'C':
    print(div(*numbers))
elif pref == 'D':
    print(mul(*numbers))
        



