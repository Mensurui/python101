#any amount of non keyword arguments
def sum_of (*args):
    sum = 0
    for x in args:
        sum += x
    return sum

print(sum_of(88, 100, 100))

#any amount of keyword arguments
def sum_of_bill (**kwargs):
    sum = 0
    for k,v in kwargs.items():
        sum += v
    return round(sum, 2)

print(sum_of_bill(onions=88.9, tomato=10.50, potato=10.80))