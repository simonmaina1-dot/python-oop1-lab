#!/usr/bin/env python3

class Book:
    """Represents a book in the bookstore with title and page count."""
    
    def __init__(self, title, page_count):
        """Initialize a Book instance with title and page_count.
        
        Args:
            title: The title of the book (string)
            page_count: The number of pages in the book (integer)
        """
        self.title = title
        self.page_count = page_count
    
    @property
    def page_count(self):
        """Get the page count of the book."""
        return self._page_count
    
    @page_count.setter
    def page_count(self, value):
        """Set the page count with validation.
        
        Args:
            value: The page count value to set
            
        Prints error message if value is not an integer.
        """
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")
    
    def turn_page(self):
        """Simulate turning a page in the book.
        
        Prints a message indicating the page has been turned.
        """
        print("Flipping the page...wow, you read fast!")

