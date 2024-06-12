from library import Library
from reader import Reader

def main():
    library = Library()
    reader = Reader("Default Reader")

    while True:
        print("\nLibrary Menu")
        print("1. Add a book")
        print("2. Remove a book by year")
        print("3. List all books")
        print("4. Borrow a book")
        print("5. Return a book")
        print("6. List all borrowed books")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter book name: ")
            author = input("Enter book author: ")
            year = int(input("Enter book year: "))
            book_type = input("Enter book type: ")
            library.add_book(name, author, year, book_type)
            print("Book added successfully.")
        elif choice == '2':
            year = int(input("Enter book year to remove: "))
            library.remove_book(year)
            print("Book removed successfully.")
        elif choice == '3':
            books = library.list_books()
            print("\nList of books in the library:")
            for book in books:
                print(book)
        elif choice == '4':
            name = input("Enter book name to borrow: ")
            book = reader.borrow_book(library, name)
            if book:
                print("Book borrowed successfully.")
            else:
                print("Book not found.")
        elif choice == '5':
            name = input("Enter book name to return: ")
            book = reader.return_book(library, name)
            if book:
                print("Book returned successfully.")
            else:
                print("Book not found or not borrowed.")
        elif choice == '6':
            borrowed_books = reader.list_borrowed_books()
            print("\nList of borrowed books:")
            for book in borrowed_books:
                print(book)
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()