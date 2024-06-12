from book import Book, save_books, load_books

class Library:
    def __init__(self):
        self.books = load_books()
        self.borrowed_books = []

    def add_book(self, name, author, year, book_type):
        book = Book(name, author, year, book_type)
        self.books.append(book)
        save_books(self.books)

    def remove_book(self, year):
        self.books = [book for book in self.books if book.year != year]
        save_books(self.books)

    def list_books(self):
        return self.books

    def borrow_book(self, name):
        for book in self.books:
            if book.name == name:
                self.books.remove(book)
                self.borrowed_books.append(book)
                save_books(self.books)
                return book
        return None

    def return_book(self, name):
        for book in self.borrowed_books:
            if book.name == name:
                self.borrowed_books.remove(book)
                self.books.append(book)
                save_books(self.books)
                return book
        return None

    def list_borrowed_books(self):
        return self.borrowed_books