def ispresent(person):
    names = {"Alice", "Bob", "Chris", "Michael"}
    if person in names:
        return True
    else:
        return False
    
from math import pi
print(pi)

sample_dict ={1:'coffee',2:'Tea', 3:'cupcake'}

for key, value in sample_dict.items():
    print(key, value)
    
def recurssion(number):
    print(number)
    next= number-3
    if next > 1:
        recurssion(next)
        
recurssion(11)

num =1
class Car:
    num =5
    bathrooms=2

def cost_evaluation(num):
    num = 10
    return num

class Bike():
    num=11
    
    
cost_evaluation(num)
car = Car()
bike = Bike()
car.num = 7
car.num =2
print(num)

def d():
    color = "green"
    def e():
        nonlocal color
        color = "yellow"
        
    e()
    print("Color: " + color)
    color = "red"
        
color = "blue"
d()