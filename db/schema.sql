
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS cart;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  firstName TEXT NOT NULL,
  lastName TEXT NOT NULL,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  isAdmin BOOLEAN NOT NULL
);

CREATE TABLE cart (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  userId INTEGER NOT NULL,
  itemId INTEGER NOT NULL,
  quantity INTEGER NOT NULL,
  FOREIGN KEY (userId) REFERENCES user(id)
);


-- Vložení cvičných záznamů do tabulky user
INSERT INTO user (firstName, lastName, username, password, isAdmin) VALUES
('Martin', 'Kapcala', 'martinkap', 'password123', 1),
('John', 'Doe', 'johndoe', 'password123', 0),
('Jane', 'Smith', 'janesmith', 'password456', 1),
('Alice', 'Johnson', 'alicej', 'password789', 0);

-- Vložení cvičných záznamů do tabulky cart
INSERT INTO cart (userId, itemId, quantity) VALUES
(1, 101, 2),
(2, 102, 1),
(3, 103, 5);