import sqlite3
import datetime

db = 'test7.db'

def execute_query(db, query, params=()):
    try:
        with sqlite3.connect(db) as connection:
            cursor = connection.cursor()
            cursor.execute(query, params)
            connection.commit()
    except sqlite3.Error as e:
        print("Error executing query:", e)

def fetch_query(db, query, params=()):
    try:
        with sqlite3.connect(db) as connection:
            cursor = connection.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()
    except sqlite3.Error as e:
        print("Error fetching data:", e)
        return []

def add_book(db, name, author, year_made, book_type):
    try:
        execute_query(db, 'INSERT INTO Book (name, author, year_made, type) VALUES (?, ?, ?, ?)', (name, author, year_made, book_type))
        print("Book added successfully!")       
    except sqlite3.Error as e:
        print("Error adding book:", e)

def remove_book(db, name):
    try:
        execute_query(db, "DELETE FROM Book WHERE name=?", (name,))
        print("Book removed successfully!")
    except sqlite3.Error as e:
        print("Error removing book:", e)

def search_book(db, search_term):
    try:
        results_name = fetch_query(db, "SELECT * FROM Book WHERE name LIKE ?", ('%' + search_term + '%',))
        results_author = fetch_query(db, "SELECT * FROM Book WHERE author LIKE ?", ('%' + search_term + '%',))
        results = results_name + results_author
        return results
    except sqlite3.Error as e:
        print("Error searching for books:", e)
        return []

def rent_book(db, renter, name):
    try:
        book_result = fetch_query(db, "SELECT * FROM Book WHERE name=?", (name,))
        
        if not book_result:
            print("Book not found in the database.")
            return
        
        book_id = book_result[0][0]
        
        user_result = fetch_query(db, "SELECT * FROM User WHERE name=?", (renter,))
        
        if not user_result:
            execute_query(db, "INSERT INTO User (name) VALUES (?)", (renter,))
            user_id = fetch_query(db, "SELECT last_insert_rowid()")[0][0]
        else:
            user_id = user_result[0][0]

        rented_date = datetime.date.today()
        due_date = rented_date + datetime.timedelta(days=14)
        
        execute_query(db, "INSERT INTO Rented (book_id, rented_date, user_id, due_date) VALUES (?, ?, ?, ?)",
                       (book_id, rented_date, user_id, due_date))
        print(f"Book rented successfully by {renter}!")
    except sqlite3.Error as e:
        print("Error renting book:", e)

def return_book(db, renter, name):
    try:
        user_result = fetch_query(db, "SELECT * FROM User WHERE name=?", (renter,))
        if not user_result:
            print("User not found in the database.")
            return
        
        user_id = user_result[0][0]
    
        book_result = fetch_query(db, "SELECT * FROM Book WHERE name=?", (name,))
        if not book_result:
            print("Book not found in the database.")
            return
        
        book_id = book_result[0][0]
        
        execute_query(db, "DELETE FROM Rented WHERE user_id=? AND book_id=?", (user_id, book_id))
        print(f'Book {name} returned successfully by {renter}')
    except sqlite3.Error as e:
        print("Error returning book:", e)


add_book(db, "1984", "George Orwell", 1949, "Comedy")
add_book(db, "mes", "auto", 1995, "Comedy")
remove_book(db, "1984")
print(search_book(db, "Orwell"))
rent_book(db, 'dovis', 'mes')
return_book(db, 'dovis', 'mes')

