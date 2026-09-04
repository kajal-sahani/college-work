"""
Lab Exercise 5 - Program 2
Library Management System using OOP
Student: Kajal
"""

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = False

    def __str__(self):
        status = "Issued" if self.is_issued else "Available"
        return f"[{self.book_id}] {self.title} by {self.author} - {status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"✅ Book '{book.title}' added.")

    def display_books(self):
        if not self.books:
            print("No books in library.")
            return
        print("\n----- Library Books -----")
        for book in self.books:
            print(book)

    def issue_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if not book.is_issued:
                    book.is_issued = True
                    print(f"✅ Book '{book.title}' issued successfully.")
                else:
                    print("Book is already issued.")
                return
        print("Book not found.")

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.is_issued:
                    book.is_issued = False
                    print(f"✅ Book '{book.title}' returned successfully.")
                else:
                    print("Book was not issued.")
                return
        print("Book not found.")


print("=" * 50)
print("      LIBRARY MANAGEMENT SYSTEM")
print("=" * 50)

lib = Library()

# Add some sample books
lib.add_book(Book(101, "Python Crash Course", "Eric Matthes"))
lib.add_book(Book(102, "Clean Code", "Robert C. Martin"))
lib.add_book(Book(103, "Introduction to Algorithms", "CLRS"))

while True:
    print("\n1. Display all books")
    print("2. Issue a book")
    print("3. Return a book")
    print("4. Add new book")
    print("5. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        lib.display_books()
    elif choice == '2':
        bid = int(input("Enter Book ID to issue: "))
        lib.issue_book(bid)
    elif choice == '3':
        bid = int(input("Enter Book ID to return: "))
        lib.return_book(bid)
    elif choice == '4':
        bid = int(input("Book ID: "))
        title = input("Title: ")
        author = input("Author: ")
        lib.add_book(Book(bid, title, author))
    elif choice == '5':
        print("Exiting Library System.")
        break
    else:
        print("Invalid choice!")
