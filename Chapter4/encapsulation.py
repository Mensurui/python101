#The idea of encapsulation is to have methods and variables
#within the bounds of a single unit in the case of python that unit is known as class

class Alpha:
    def __init__(self):
        self._a = 2. #Protected member 'a' '_'
        self.__b = 2. #Private member 'b' '__'
    def get_b(self):
        return self.__b

    #def set_b(self, value):
        #self.__b = value

#You can be able to access it by some twitching
obj = Alpha()
valueA = obj._a

valueB = obj.get_b()

print(valueA)
print(valueB)

