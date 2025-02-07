
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