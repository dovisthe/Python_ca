CREATE TABLE `User` (
  `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `name` text(20) NOT NULL
);

CREATE TABLE `Book` (
  `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `name` text NOT NULL,
  `author` text NOT NULL,
  `year_made` integer NOT NULL,
  `type` text NOT NULL
);

CREATE TABLE `Rented` (
  `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `book_id` text NOT NULL,
  `rented_date` date NOT NULL,
  `user_id` text NOT NULL,
  `return_date` date,
  `due_date` date NOT NULL,
  FOREIGN KEY (`book_id`) REFERENCES `Book` (`id`),
  FOREIGN KEY (`user_id`) REFERENCES `User` (`id`)
);


