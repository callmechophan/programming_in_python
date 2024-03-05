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





# display all in menu
def display_menu():
    print("----------MENU----------")
    for key, value in menu.items():
        print(f"{key}. {value['name'] : <9} | {value['price'] : >5}") # use single quote when access a set
    print()





# create an order by prompting the user to select menu items
def take_order():
    """
    Returns:
        order (list): list of dicts that contain an item name and price from menu
    """

    display_menu()
    
    order = []
    count = 1
    for i in range(3):
        item = input(f"Select menu item number {count} (from 1 to 5): ")
        count += 1
        order.append(menu[int(item)])

    return order





def print_order(order: list):
    print("\nYou have orderd 3 items: ")
    items = []
    items = [item['name'] for item in order] # use a short for loop
    print(f"{items}")





def calculate_subtotal(order: list):
    """
    Description:
        The sum of the prices of the items in the order
        
    Args:
        order: list of dicts that contain an item name and price from menu

    Returns:
        subtotal
    """

    print("\nCalculating bill subtotal...")
    ### WRITE SOLUTION HERE
    subtotal = 0
    for i in order:
        subtotal += i["price"]

    return round(subtotal, 2)





def calculate_tax(subtotal: float):
    """
    Description:
        The tax required of a given subtotal, which is 15% rounded to two decimals

    Args:
        subtotal: the price to get the tax of

    Returns:
        tax (float): variable (float rounded)
    """

    print("\nCalculating bill tax...")
    tax = subtotal * 0.15

    return round(tax, 2)





def summarize_order(order: list):
    """
    Description:
        1. Calculate the total (subtotal + tax) and store it in a variable named total (rounded to two decimals)
        2. Store only the names of all the items in the order in a list named names
        3. Return names and total
    
    Args:
        order: list of dicts that contain an item name and price from menu

    Returns:
        names
        total
    """

    names = []
    for i in order:
        names.append(i["name"])

    subtotal = calculate_subtotal(order)
    print("Subtotal for the order is:", subtotal)

    tax = calculate_tax(subtotal)
    print("Tax for the order is:", tax)

    total = subtotal + tax

    return names, round(total, 2)





def main():
    order = take_order()
    print_order(order)

    _, total = summarize_order(order)
    print("\nTotal is:", total)

if __name__ == "__main__":
    main()
