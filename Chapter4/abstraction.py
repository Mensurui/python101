#Used for both hiding important and unnecessary information
#It is implemented in ppython using abstract class and methods which we 
#can implement by importing the abc module i.e. abstract base class

from abc import ABC

class abstractClass(ABC):
    def __init__(self):
        print("abstractClass constructor")

obj = abstractClass()