class Recipe():
    def __init__(self, dish, items, time):
        self.dish = dish
        self.items = items
        self.time = time
    
    def contents(self):
        print("The " + self.dish + " has" + str(self.items) + \
            " and takes " + str(self.time) + " to cook")
        pass
    
pizza = Recipe("Pizza", ["Cheese", "Tomato", "Bread"], 45)
pasta = Recipe("Pasta", ["pine", "sauce"], 55)

pizzaI = pizza.items
pastaD = pasta.dish

print(pastaD)
print(pizzaI)

pizzaContents = pizza.contents()
pastaContents = pasta.contents()

