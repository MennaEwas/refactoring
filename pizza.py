""
Mennatullah Abdelrahman 
120180009
Lab3
Software Lab
Date : 4/8/2021
"""

#pizza 
from enum import Enum
class PizzaSize(Enum):
     # write the sizes and their values
     # one per line
     small = 120
     medium = 200
     large = 280
     
     def __str__(self):
         return self.name 
     
     def price(self,toppings):
        """Calculating the price of the pizza"""
        base_top=len(toppings)
        base_to_topping = {120: 20, 200: 25, 280: 30}                   # base_price 
        topping_price=lambda base_price:base_to_topping[base_price]     # get topping price
        return self.value+base_top*topping_price(self.value)
            
class Pizza:
    """A pizza with a size and optional toppings."""
    Small = 'small'
    Med = 'medium'
    Large = 'large'

    def __init__(self, size: str):
        self.size = size
        self.toppings = []


    def get_price(self):
        return self.size.price(self.toppings)
       
    
    def add_topping(self, topping):
        """Add a topping to the pizza"""
        if topping not in self.toppings:
            self.toppings.append(topping)
            
    def test_pizza_sizes(self):
        for size in PizzaSize:
            print(size, "pizza price:",size.value)

#Extract Method
    
    def __str__(self):
        if self.toppings:
            description = "pizza with " + ", ".join(self.toppings)
        else: 
            description = 'plain pizza'
        return f'A {self.size} {description}'

