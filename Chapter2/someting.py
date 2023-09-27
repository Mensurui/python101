menu = {
    1: {"name": 'espresso',
        "price": 1.99},
    2: {"name": 'coffee', 
        "price": 2.50},
    3: {"name": 'cake', 
        "price": 2.79},
    4: {"name": 'soup', 
        "price": 4.50},
    5: {"name": 'sandwich',
        "price": 4.99}
}

def calculate_subtotal(order):
    """ Calculates the subtotal of an order

    [IMPLEMENT ME] 
        1. Add up the prices of all the items in the order and return the sum.

    Args:
        order: list of item numbers (keys in the menu dictionary)

    Returns:
        float: The sum of the prices of the items in the order
    """
    subtotal = sum(menu[item]["price"] for item in order)
    return subtotal

def calculate_tax(subtotal):
    """ Calculates the tax of an order

    [IMPLEMENT ME] 
        1. Multiply the subtotal by 15% and return the product rounded to two decimals.

    Args:
        subtotal: the price to get the tax of

    Returns:
        float - The tax required of a given subtotal, which is 15% rounded to two decimals.
    """
    tax = subtotal * 0.15
    return round(tax, 2)

def summarize_order(order):
    """ Summarizes the order

    [IMPLEMENT ME]
        1. Calculate the total (subtotal + tax) and store it in a variable named total (rounded to two decimals).
        2. Store only the names of all the items in the order in a list called names.
        3. Return names and total.

    Args:
        order: list of item numbers (keys in the menu dictionary)

    Returns:
        tuple of names and total.
    """
    names = [menu[item]["name"] for item in order]
    subtotal = calculate_subtotal(order)
    tax = calculate_tax(subtotal)
    total = round(subtotal + tax, 2)
    return names, total

# This function is provided for you, and will print out the items in an order
def print_order(order):
    print('You have ordered ' + str(len(order)) + ' items')
    items = [menu[item]["name"] for item in order]
    print(items)

# This function is provided for you, and will display the menu
def display_menu():
    print("------- Menu -------")
    for selection in menu:
        print(f"{selection}. {menu[selection]['name'] : <9} | {menu[selection]['price'] : >5}")
    print()

# This function is provided for you, and will create an order by prompting the user to select menu items
def take_order():
    display_menu()
    order = []
    count = 1
    for i in range(3):
        item = int(input('Select menu item number ' + str(count) + ' (from 1 to 5): '))
        if item in menu:
            order.append(item)
            count += 1
        else:
            print("Invalid menu item number. Please select a valid item.")
    return order

# Sample function calls to test your code
def main():
    order = take_order()
    print_order(order)
    names, total = summarize_order(order)
    print("Item names:", names)
    print("Total cost: $", total)

if __name__ == "__main__":
    main()
