#The inputs needed are:
    #water 
    #coffee
#the edge cases are:
    #sugar
    #milk
#steps include:
    #boiling the water
    #adding the coffee to the boiling water
#edge case steps:
    #adding milk to the coffee
    #adding sugar to the coffee
    #adding both sugar and milk to the coffee
    #adding nothing to the coffee

def coffee_process(water, coffee):
    if water:
        print("water is boiling")
    elif coffee:
        print("coffee is added to the container")
        print("wait for some minutes")
        cse = input("What do you want to add as a topping to the container \n" +"Milk\n"+"Sugar\n"+"Both\n"+"Or Neither\n")
        if cse == "Milk":
           print("Milk is added to the container \n" + "Enjoy your drink\n")
        elif cse == "Sugar":
            print("Sugar is added to the container \n" + "Enjoy your drink\n")
        elif cse == "Both":
            print("Both are added to the container \n" + "Enjoy your drink\n")
        else:
            print("Neither is added to the container \n" + "Enjoy your drink\n")

            
            
water = input('Add water to the boiler: ')
coffee_process(water, "")
coffee = input('Add Coffee to the boiling water: ')
coffee_process("", coffee)


