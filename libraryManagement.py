class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f'"{book.title}" added to library.')

    def display_books(self):
        if not self.books:
            print("No books in the library.")
            return
        for book in self.books:
            status = "Borrowed" if book.is_borrowed else "Available"
            print(f'{book.title} by {book.author} - {status}')

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.is_borrowed:
                book.is_borrowed = True
                print(f'You borrowed "{book.title}".')
                return
        print("Book not available or already borrowed.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.is_borrowed:
                book.is_borrowed = False
                print(f'You returned "{book.title}".')
                return
        print("Book not found or was not borrowed.")

library = Library()
book1 = Book("1984", "George Orwell")
book2 = Book("Python Basics", "John Doe")

library.add_book(book1)
library.add_book(book2)
library.display_books()
library.borrow_book("1984")
library.display_books()
library.return_book("1984")
library.display_books()


