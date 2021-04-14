""
Mennatullah Abdelrahman 
120180009
Lab3
Software Lab
Date : 4/8/2021
"""
#pizzaShop
from pizza import Pizza, PizzaSize

# This function shows a limitation on tool-assisted
# refactoring in a dynamic language like Python.
#
# When you rename the Pizza get_price method to get_price,
# does it rename the method here?
# - if no type annotation on the pizza parameter, maybe not
# - if use type annotation ':Pizza' on the parameter, it should

def print_pizza( pizza ):
    """
    Print a description of a pizza, along with its price.
    """

    print(pizza)
    print("Price {:6.2f}".format(pizza.get_price()))
    

if __name__ == "__main__":
    pizza = Pizza(PizzaSize.small)
    pizza.add_topping("mushroom")
    pizza.add_topping("tomato")
    pizza.add_topping("pinapple")
    print_pizza(pizza)

    pizza2 = Pizza(PizzaSize.medium)
    print_pizza(pizza2)

    pizza3 = Pizza(PizzaSize.large)
    pizza3.add_topping("seafood")
    print_pizza(pizza3)
