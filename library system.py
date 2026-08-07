class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.issued = False

    
    def display(self):
        status = "Issued" if self.issued else "Available"
        print(f"Book ID : {self.book_id}")
        print(f"Title   : {self.title}")
        print(f"Author  : {self.author}")
        print(f"Status  : {status}")
        print("-" * 30)


class Library:
    def __init__(self):
        self.books = []

    
    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully!\n")

    
    def view_books(self):
        if len(self.books) == 0:
            print("No books available.\n")
        else:
            print("\nLibrary Books")
            print("=" * 30)
            for book in self.books:
                book.display()

    def issue_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if not book.issued:
                    book.issued = True
                    print("Book issued successfully!\n")
                else:
                    print("Book is already issued.\n")
                return
        print("Book ID not found.\n")



library = Library()

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        n = int(input("Enter number of books to add: "))

        for i in range(n):
            print(f"\nEnter details for Book {i + 1}")
            book_id = int(input("Book ID: "))
            title = input("Book Title: ")
            author = input("Author Name: ")

            book = Book(book_id, title, author)
            library.add_book(book)

    elif choice == "2":
        library.view_books()

    elif choice == "3":
        book_id = int(input("Enter Book ID to issue: "))
        library.issue_book(book_id)

    elif choice == "4":
        print("Thank you for using Library Management System.")
        break

    else:
        print("Invalid choice. Please try again.")