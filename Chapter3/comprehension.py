#LIST COMPREHENSION

listName =  ["list comprehension"]
newlistname = []

for x in listName:
    if x != "":
        newlistname = x.upper()
    print(newlistname)

data = [2,3,5,7,11,13,17,19,23,29,31]

# Ex1: List comprehension: updating the same list
data = [x+3 for x in data]
print("Updating the list: ", data)

# Ex2: List comprehension: creating a different list with updated values
new_data = [x*2 for x in data]
print("Creating new list: ", new_data)

# Ex3: With an if-condition: Multiples of four:
fourx = [x for x in new_data if x%4 == 0 ]
print("Divisible by four", fourx)

# Ex4: Alternatively, we can update the list with the if condition as well
fourxsub = [x-1 for x in new_data if x%4 == 0 ]
print("Divisible by four minus one: ", fourxsub)

# Ex5: Using range function:
nines = [x for x in range(100) if x%9 == 0]
print("Nines: ", nines)

#DICTIONARY COMPREHENSION
#dict = { key:value for key, value in <sequence> if <condition> } 
# Using range() function and no input list
listName =  ["DICTIONARY COMPREHENSION"]
newlistname = []

for x in listName:
    if x != "":
        newlistname = x.upper()
    print(newlistname)
    
usingrange = {x:x*2 for x in range(12)}
print("Using range(): ",usingrange)

# Lists
months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
number = [1,2,3,4,5,6,7,8,9,10,11,12]

# Using one input list
numdict = {x:x**2 for x in number}
print("Using one input list to create dict: ", numdict)

# Using two input lists
months_dict = {key:value for (key, value) in zip(number, months)}
print("Using two lists: ", months_dict)

#SET COMPREHENSION
print("SET COMPREHENSION")
set_a = {x for x in range(10,20) if x not in [12,14,16]}
print(set_a)


a=[[96], [69]]
print(''.join(list(map(str, a))))

z = ["alpha", "bravo", "charlie"]
new_z = [i[0]*2 for i in z]
print(new_z)

def sum(n):
    if n == 1:
        return 0
    print (n)
    return n + sum(n-1)

a = sum(5)
print(a)

some = ["aaa", "bbbb"]

def aa ():
    return "aaa"

