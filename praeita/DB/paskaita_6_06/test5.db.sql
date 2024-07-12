BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "User" (
	"id"	INTEGER NOT NULL,
	"name"	TEXT NOT NULL,
	"rented_id"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("rented_id") REFERENCES "Rented"("id")
);
CREATE TABLE IF NOT EXISTS "Library" (
	"id"	INTEGER NOT NULL,
	"book_id"	TEXT,
	"user_id"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("book_id") REFERENCES "Book"("id"),
	FOREIGN KEY("user_id") REFERENCES "User"("id")
);
CREATE TABLE IF NOT EXISTS "Book" (
	"id"	INTEGER NOT NULL,
	"name"	TEXT,
	"author"	TEXT,
	"year_made"	INTEGER,
	"type"	TEXT,
	"quantity"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Rented" (
	"id"	INTEGER NOT NULL,
	"book_id"	INTEGER,
	"rented_date"	DATE,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("book_id") REFERENCES "Book"("id")
);
COMMIT;
