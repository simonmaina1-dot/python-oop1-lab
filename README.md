# Object Oriented Programming Lab - Bookstore

This scenario encompasses all of the topics provided in the module. This project demonstrates creating new classes in Python by building two different classes to represent and model a bookstore.

## The Scenario

You are tasked with building two different classes to aid with representing and modeling a bookstore. First is a book object to allow for reading an online book and the second is a coffee object as another item carried by the store. Both objects have several attributes and methods.

## Functionality

This application provides two Python classes:

### Book Class
- **Attributes:**
  - `title`: The title of the book (required)
  - `page_count`: The number of pages in the book (required, must be an integer)
- **Methods:**
  - `turn_page()`: Prints "Flipping the page...wow, you read fast!"

### Coffee Class
- **Attributes:**
  - `size`: The size of the coffee (required, must be Small, Medium, or Large)
  - `price`: The price of the coffee (required)
- **Methods:**
  - `tip()`: Prints "This coffee is great, here's a tip!" and increases the price by 1

## Usage

```python
from lib.book import Book
from lib.coffee import Coffee

# Create a book
book = Book("And Then There Were None", 272)
print(book.title)  # And Then There Were None
print(book.page_count)  # 272
book.turn_page()  # Flipping the page...wow, you read fast!

# Create a coffee
coffee = Coffee("Large", 3.50)
print(coffee.size)  # Large
print(coffee.price)  # 3.5
coffee.tip()  # This coffee is great, here's a tip!
print(coffee.price)  # 4.5
```

## Testing

Run all tests:
```console
pytest
```

Run Book tests:
```console
pytest lib/testing/book_test.py
```

Run Coffee tests:
```console
pytest lib/testing/coffee_test.py
```

## Tools & Resources

* [GitHub Repo](https://github.com/learn-co-curriculum/python-oop1-lab)
* [Python Classes](https://docs.python.org/3/tutorial/classes.html)

