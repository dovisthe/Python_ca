CREATE TABLE IF NOT EXISTS `User` (
  `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `name` TEXT NOT NULL,
  `rented_id` TEXT,
  FOREIGN KEY ('rented_id') REFERENCES 'Rented' ('id')
);

CREATE TABLE IF NOT EXISTS `Library` (
  `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `book_id` TEXT,
  `user_id` TEXT,
  FOREIGN KEY (`book_id`) REFERENCES `Book` (`id`),
  FOREIGN KEY (`user_id`) REFERENCES `User` (`id`)
);

CREATE TABLE IF NOT EXISTS `Book` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  `name` TEXT,
  `author` TEXT,
  `year_made` INTEGER,
  `type` TEXT,
  `quantity` TEXT
);

CREATE TABLE IF NOT EXISTS `Rented` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  `book_id` INTEGER,
  `rented_date` DATE,
  FOREIGN KEY (`book_id`) REFERENCES `Book` (`id`)
);
