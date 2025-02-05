
tuple_menu = ("Pizza", "Burger", "Pasta", "Salad", "Cookie")


def print_menu(menu):
    print("Menu:")
    for item in menu:
        print("-", item)

print_menu(tuple_menu)


try:
    tuple_menu[0] = "Brownie"
except TypeError as e:
    print("\nError:", e)

new_menu = ("Brownie", "Burger", "Pasta", "Tacos", "Cookie")


print("\nUpdated Menu:")
print_menu(new_menu)
