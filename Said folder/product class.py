""" Create product class eac product has name , category, and price --> instance vaiable 
class is able to return a discribtion of product --> method
for each product be abke ti compute discount of  given mount (compute price after dscount of amount%)
"""

class Product :
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price
    def discribtion(self):
        x = f''' name is {self.name}
        category is {self.category}
        price is {self.price}'''
        
        return x
    def discount(self, discount):
        self.price = self.price - (self.price * discount)
        
        
        