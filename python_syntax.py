#This is a comment

name, name1 = "John", "Johnny"
numbers = [1, 2, 3, 4, 5, 6]
def sayHello(): print("Hello " + name)
def sayHello2(): print("Hello " + name1)
if name == "John": print(sayHello()) 
else:print('You are wrong. Please enter your name here instead of ' + name)
del name
if name1 == "Johnny": print(sayHello2())
else:print('You are wrong. Please enter your name here instead of ' + name1)
del name1
print(numbers[1])

j=4
a = 10 +10*j
print(a)

naming = "hello world"
print(naming[0])
print(type(naming))

Dictionary = {"alpha": ["a,b,c"],  "beta":[1,2,3], "gama":"mensur", "delta":1}
print(Dictionary["beta"])
print(type(Dictionary))

string = "hello world"\
            "this is a multi-line string"\
            "and this is a multi-line string too"\
            "and this is a multi-line string too"
 
print(len(string))
            
if len(string) > 108 : print(string)
else : print("it is less than 108 characters")

print("write your name")
enum= input()
print("Is your name " + enum.capitalize() + "?")

yesOrNo = input()
if yesOrNo == "yes": print(":() damn your parents don't like you")
def addition(numberOne, numberTwo):
    return (numberOne+numberTwo)

numberOne = int(input("Please enter a number"))
numberTwo = int(input("Please another number"))
guessTheSum = int(input("Please enter a guess"))
result = str(addition(numberOne, numberTwo))
if str(guessTheSum) == result : print("Damn son you are correct")
else: print("Stupiddddddd the answer is " + result)

print("Hello", "you", sep=',')
names = input("Please enter your first name")
namer = input("Please enter your second name")
print("Hello {1} {0}".format(names.capitalize(), namer.capitalize()) )

