# Task 1: Restaurant Menu Update


def add_category(menu, category):
    if category not in menu:
        menu[category] = {}
        print(f"Category '{category}' added to menu.")
        
def add_item(menu, category, item, price):
    if category in menu:
        if item not in menu[category]:
            menu[category][item] = price
            print(f"Item '{item}' added to '{category}'.")
        else:
            print(f"Item '{item}' already exists in '{category}'.")
    print(f"new menu {menu}")

def update_price(menu, category, item, price):
    if category in menu and item in menu[category]:
        menu[category][item] = price
        updated_price = menu[category][item]
        print(f"Price of Item '{item}' updated to '{updated_price}'.")
    else:
        print(f"Category '{category}' does not exist.")

def remove_item(menu, category, item):
    if category in menu and item in menu[category]:
        del menu[category][item]
        print(f"Item '{item}' removed.")
    else:
        print(f"Item or category not found.")

restaurant_menu = {
    "Starters" : {"Soup" : 5.99, "Bruschetta": 6.50},
    "Main Course" : {"Steak" : 15.99, "Salmon" : 13.99},
    "Desserts" : {"Cake" : 4.99, "Ice Cream" : 3.99}
}

add_category(restaurant_menu, "Beverages")
add_item(restaurant_menu, "Beverages", "Water", 0.00)
add_item(restaurant_menu, "Beverages", "Tea", 2.99)
update_price(restaurant_menu, "Main Course", "Steak", 17.99)
remove_item(restaurant_menu, "Starters", "Bruschetta")