class Reader:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, library, book_name):
        book = library.borrow_book(book_name)
        if book:
            self.borrowed_books.append(book)
        return book

    def return_book(self, library, book_name):
        for book in self.borrowed_books:
            if book.name == book_name:
                self.borrowed_books.remove(book)
                library.return_book(book_name)
                return book
        return None

    def list_borrowed_books(self):
        return self.borrowed_books