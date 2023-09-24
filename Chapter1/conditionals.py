bill_total = 100

if bill_total == 100 :
    print ("Total bill is met")
elif bill_total > 100 :
    print ("Total bill isgreater than 100")
else :
    print ("Total bill is less than 100")
    
ills = ['Happy', 'Pending', 'outstanding']

for item in ills :
    print("I like - ", item)
    
favorites = ['Creame Brulle', "Apple Pie", "Churros", "Tiramisu", "Chocolate Cake"]
for items in favorites :
    print("I like this dessert - ", items)
bill = int(input())

number_of_bills = len(favorites)

while bill < number_of_bills: 
    print("You are right the amount of favorites is-", favorites[bill])
    bill+=bill;
    
https= int(input())
 
print(type(https))
match https:
     case 101|100:
         print("Error in request")
     case 201|200:
         print("Success in request")
     case 301|300:
         print("Error in download request")
     case _:
         print("Error unknown request")