import pickle

class Book:
    def __init__(self, name, author, year, book_type):
        self.name = name
        self.author = author
        self.year = year
        self.book_type = book_type

    def __repr__(self):
        return f"Book(name={self.name}, author={self.author}, year={self.year}, type={self.book_type})"

def save_books(books, filename='books.pkl'):
    with open(filename, 'wb') as f:
        pickle.dump(books, f)

def load_books(filename='books.pkl'):
    try:
        with open(filename, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return []