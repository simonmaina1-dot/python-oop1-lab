#!/usr/bin/env python3

class Coffee:
    """Represents a coffee item in the bookstore with size and price."""
    
    def __init__(self, size, price):
        """Initialize a Coffee instance with size and price.
        
        Args:
            size: The size of the coffee (Small, Medium, or Large)
            price: The price of the coffee (numeric value)
        """
        self.size = size
        self.price = price
    
    @property
    def size(self):
        """Get the size of the coffee."""
        return self._size
    
    @size.setter
    def size(self, value):
        """Set the coffee size with validation.
        
        Args:
            value: The size value to set
            
        Prints error message if value is not Small, Medium, or Large.
        """
        if value in ["Small", "Medium", "Large"]:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")
    
    def tip(self):
        """Simulate giving a tip for the coffee.
        
        Prints a message about the tip and increases the price by 1.
        """
        print("This coffee is great, here\u2019s a tip!")
        self.price += 1

