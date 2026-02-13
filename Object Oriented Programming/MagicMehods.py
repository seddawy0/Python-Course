# Dunder methods (double underscore) __init__, __str__, __eq__
# They are automatically called by many of Python's built-in operations
# They allow developer to define or customize the behavior of objects
print("#################### Magic Methods #####################")
class Book:
    def __init__(self, title, author, num_pages): # Will give us the place in the memory
        self.title = title
        self.author = author
        self.num_pages = num_pages
    def __str__(self): # Will give us a string
        return f"'{self.title}' by {self.author}"
    def __eq__(self, other): 
        return self.title == other.title and self.author == other.author
    def __lt__(self, other):
        return self.num_pages < other.num_pages
    def __gt__(self, other):
        return self.num_pages > other.num_pages
    def __add__(self, other):
        return self.num_pages + other.num_pages
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    def __getitem__(self, key):
        if key == "title":
            return f"Title: {self.title}"
        elif key == "author":
            return f"Author: {self.author}"
        elif key == "num_pages":
            return f"Number of Pages: {self.num_pages}"
        else:
            return f"Key {key} was not found"
    
book1 = Book(title="The Hobbit", author="J.R.R.", num_pages=315)
book2 = Book(title="Harry Potter", author="J.K. Rowling", num_pages=223)
book3 = Book(title="The Lion, The Witch, and The Wardrobe", author="C.S. Lewis", num_pages=460)

print("---------------------")
print(book1)
print(book2)
print(book3)
print()

print("---------------------")
book4 = Book(title="The Hobbit", author="J.R.R.", num_pages=315)
book5 = Book(title="The Hobbit", author="J.R.R.", num_pages=223)
book6 = Book(title="Harry Potter", author="J.K. Rowling", num_pages=550)
print(f"Is this book equal the other book?: {book4 == book5}")
print(f"Is this book equal the other book?: {book5 == book6}")
print()

print("---------------------")
book1 = Book(title="The Hobbit", author="J.R.R.", num_pages=315)
book2 = Book(title="Harry Potter", author="J.K. Rowling", num_pages=223)
book3 = Book(title="The Lion, The Witch, and The Wardrobe", author="C.S. Lewis", num_pages=460)
print(f"Is this book less than the other book?: {book1 < book2}")
print(f"Is this book less than the other book?: {book2 < book3}")
print(f"Is this book less than the other book?: {book3 < book1}")
print()

print("---------------------")
book1 = Book(title="The Hobbit", author="J.R.R.", num_pages=315)
book2 = Book(title="Harry Potter", author="J.K. Rowling", num_pages=223)
book3 = Book(title="The Lion, The Witch, and The Wardrobe", author="C.S. Lewis", num_pages=460)
print(f"Is this book greater than the other book?: {book1 > book2}")
print(f"Is this book greater than the other book?: {book2 > book3}")
print(f"Is this book greater than the other book?: {book3 > book1}")
print()

print("---------------------")
book1 = Book(title="The Hobbit", author="J.R.R.", num_pages=315)
book2 = Book(title="Harry Potter", author="J.K. Rowling", num_pages=223)
book3 = Book(title="The Lion, The Witch, and The Wardrobe", author="C.S. Lewis", num_pages=460)
print(f"Number of pages after adding the 1st book to the 2nd book: {book1 + book2}")
print(f"Number of pages after adding the 1st book to the 2nd book: {book2 + book3}")
print(f"Number of pages after adding the 1st book to the 2nd book: {book3 + book1}")
print()

print("---------------------")
print(f"Is this book contains this word?: {"Hobbit" in book1}")
print(f"Is this book contains this word?: {"J.R.R." in book2}")
print(f"Is this book contains this word?: {"Lewis" in book3}")
print()

print("---------------------")
print(book1["title"])
print(book1["author"])
print(book1["num_pages"])
print(book1["audio"])
print("########################################################")
