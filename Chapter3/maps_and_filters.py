menu = ['espresso', 'mocha', 'latte', 'cappuccino', 'cortado', 'americano']

def find_coffee(coffee):
    if coffee[0] == 'c': print(coffee)
    
#map_coffee = map(find_coffee, menu)
#for x in map_coffee:
 #   print(x)
    
filter_coffee = filter(find_coffee, menu)
for x in filter_coffee:
    print(x)