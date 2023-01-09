### CREATE A TABLE

This project familiarizes you with the basic SQL commands. 

- Create a table called friends with three columns, id, name, and birthday.
  
  ```
  CREATE TABLE friends (id INTEGER, name TEXT, birthday DATE);
  ```

- Insert a first entry into the table.
  
  ```
  INSERT INTO friends (id, name, birthday) VALUES (1, 'Ororo Munroe', '1940-05-30');
  INSERT INTO friends (id, name, birthday) VALUES (2, 'Johny Mooney', '1960-01-01');
  INSERT INTO friends (id, name, birthday) VALUES (3, 'Honey Booney', '1955-11-05');
  ```

- View the current table.
  
  ```
  SELECT * FROM friends;
  ```

- Update row with id 1.
  
  ```
  UPDATE friends SET name='Storm Munroe' WHERE id=1;
  ```

- View current table.  
  
  ```
  SELECT * FROM friends;
  ```

- Add a new column to table.
  
  ```
  ALTER TABLE friends ADD COLUMN email TEXT;
  ```

- View current table.
  
  ```
  SELECT * FROM friends;
  ```

- Add email addresses to each row.
  
  ```
  UPDATE friends SET email='storm@codecademy.com' WHERE id=1;
  UPDATE friends SET email='johny@codecademy.com' WHERE id=2;
  UPDATE friends SET email='honey@codecademy.com' WHERE id=3;
  ```

- View current table.
  
  ```
  SELECT * FROM friends;
  ```

- Delete row with id=1.
  
  ```
  DELETE FROM friends WHERE id=1;
  ```

- View current table.
  
  ```
  SELECT * FROM friends;
  ```