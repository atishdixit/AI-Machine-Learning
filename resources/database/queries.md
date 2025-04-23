```
##
show databases;
create database pet_store;
show databases;
use pet_store;
drop database per_store;
show databases;
-- next

create database book_store;
use book_store;
CREATE TABLE books 
	(
		book_id INT AUTO_INCREMENT,
		title VARCHAR(100),
		author_fname VARCHAR(100),
		author_lname VARCHAR(100),
		released_year INT,
		stock_quantity INT,
		pages INT,
		PRIMARY KEY(book_id)
	);
 
INSERT INTO books (title, author_fname, author_lname, released_year, stock_quantity, pages)
VALUES
('The Namesake', 'Jhumpa', 'Lahiri', 2003, 32, 291),
('Norse Mythology', 'Neil', 'Gaiman',2016, 43, 304),
('American Gods', 'Neil', 'Gaiman', 2001, 12, 465),
('Interpreter of Maladies', 'Jhumpa', 'Lahiri', 1996, 97, 198),
('A Hologram for the King: A Novel', 'Dave', 'Eggers', 2012, 154, 352),
('The Circle', 'Dave', 'Eggers', 2013, 26, 504),
('The Amazing Adventures of Kavalier & Clay', 'Michael', 'Chabon', 2000, 68, 634),
('Just Kids', 'Patti', 'Smith', 2010, 55, 304),
('A Heartbreaking Work of Staggering Genius', 'Dave', 'Eggers', 2001, 104, 437),
('Coraline', 'Neil', 'Gaiman', 2003, 100, 208),
('What We Talk About When We Talk About Love: Stories', 'Raymond', 'Carver', 1981, 23, 176),
("Where I'm Calling From: Selected Stories", 'Raymond', 'Carver', 1989, 12, 526),
('White Noise', 'Don', 'DeLillo', 1985, 49, 320),
('Cannery Row', 'John', 'Steinbeck', 1945, 95, 181),
('Oblivion: Stories', 'David', 'Foster Wallace', 2004, 172, 329),
('Consider the Lobster', 'David', 'Foster Wallace', 2005, 92, 343);

INSERT INTO books(title, author_fname, author_lname, released_year, stock_quantity, pages)
VALUES ('10% Happier', 'Dan', 'Harris', 2014, 29, 256), 
           ('fake_book', 'Freida', 'Harris', 2001, 287, 428),
           ('Lincoln In The Bardo', 'George', 'Saunders', 2017, 1000, 367);
           
-- String fuction 

SELECT CONCAT('pi', 'ckle');
SELECT CONCAT('pi', 'ckle') as test ;
SELECT CONCAT(author_fname,' ', author_lname) AS author_name FROM books;
SELECT CONCAT_WS('-',title, author_fname, author_lname) AS Data FROM books;

SELECT SUBSTRING('Hello World', 1, 4) As Str;
SELECT SUBSTRING('Hello World', 7);
SELECT SUBSTRING('Hello World', -3);
SELECT SUBSTRING(title, 1, 10) AS 'short title' FROM books;
SELECT SUBSTR(title, 1, 10) AS 'short title' FROM books;

SELECT CONCAT
    (
        SUBSTRING(title, 1, 10),
        '...'
    ) AS 'short title'
FROM books;

SELECT REPLACE('Hello World', 'Hell', '%$#@');
SELECT REPLACE('Hello World', 'l', '7');
SELECT REPLACE('Hello World', 'o', '0');
SELECT REPLACE('HellO World', 'o', '*');
SELECT REPLACE('cheese bread coffee milk', ' ', ' and ');
SELECT REPLACE(title, 'e ', '3') FROM books;
SELECT REPLACE(title, ' ', '-') FROM books;

SELECT REVERSE('Hello World');
SELECT REVERSE('meow meow');
SELECT REVERSE(author_fname) FROM books;
SELECT CONCAT('woof', REVERSE('woof'));
SELECT CONCAT(author_fname, REVERSE(author_fname)) FROM books;

SELECT CHAR_LENGTH('Hello World');
SELECT CHAR_LENGTH(title) as length, title FROM books;
SELECT author_lname, CHAR_LENGTH(author_lname) AS 'length' FROM books;
SELECT CONCAT(author_lname, ' is ', CHAR_LENGTH(author_lname), ' characters long') FROM books;
select author_fname from books;
Select author_fname from books where (CHAR_LENGTH(author_fname) = 4);

SELECT UPPER('Hello World');
SELECT LOWER('Hello World');
SELECT UPPER(title) FROM books; 
SELECT CONCAT('MY FAVORITE BOOK IS ', UPPER(title)) FROM books;
SELECT CONCAT('MY FAVORITE BOOK IS ', LOWER(title)) FROM books;

SELECT INSERT('Hello Bobby', 6, 0, 'There'); 
 
SELECT LEFT('omghahalol!', 3);
SELECT RIGHT('omghahalol!', 4);
SELECT REPEAT('ha', 4);
SELECT TRIM('  pickle  ');

SELECT author_lname FROM books;
SELECT DISTINCT author_lname FROM books;
SELECT author_fname, author_lname FROM books;
SELECT DISTINCT CONCAT(author_fname,' ', author_lname) FROM books;
SELECT DISTINCT author_fname, author_lname FROM books;

SELECT * FROM books ORDER BY author_lname;
SELECT * FROM books ORDER BY author_lname DESC;
SELECT * FROM books ORDER BY released_year;
SELECT * FROM books ORDER BY released_year DESC;

-- By clumn 2
SELECT book_id, author_fname, author_lname, pages
FROM books ORDER BY 2 desc;
 
SELECT book_id, author_fname, author_lname, pages
FROM books ORDER BY author_lname, author_fname;


SELECT title FROM books LIMIT 3;
SELECT title FROM books LIMIT 1;
SELECT title FROM books LIMIT 10;
SELECT * FROM books LIMIT 1;
SELECT title, released_year FROM books ORDER BY released_year DESC LIMIT 5;
SELECT title, released_year FROM books ORDER BY released_year DESC LIMIT 1;
SELECT title, released_year FROM books ORDER BY released_year DESC LIMIT 14;
SELECT title, released_year FROM books ORDER BY released_year DESC LIMIT 0,5;
SELECT title, released_year FROM books ORDER BY released_year DESC LIMIT 0,3;
SELECT title, released_year FROM books ORDER BY released_year DESC LIMIT 1,3;
SELECT title, released_year FROM books ORDER BY released_year DESC LIMIT 10,1;
SELECT * FROM tbl LIMIT 95,18446744073709551615;
SELECT title FROM books LIMIT 5; 
SELECT title FROM books LIMIT 5, 123219476457;
SELECT title FROM books LIMIT 5, 50;
select book_id, author_fname, author_lname from books  ORDER BY 2 DESC limit 5;

select author_fname from books  where author_fname='Neil' limit 1;
SELECT title, author_fname, author_lname, pages FROM books WHERE author_fname LIKE '%da%';
SELECT title, author_fname, author_lname, pages FROM books WHERE title LIKE '%:%';
SELECT * FROM books WHERE author_fname LIKE '____';
SELECT * FROM books WHERE author_fname LIKE '_a_';

-- To select books with '%' in their title:
SELECT * FROM books WHERE title LIKE '%\%%';
 
-- To select books with an underscore '_' in title:
SELECT * FROM books WHERE title LIKE '%\_%';



SELECT title FROM books WHERE title LIKE '%stories%';
 SELECT title, pages FROM books ORDER BY pages DESC LIMIT 1;
 SELECT CONCAT(title, ' - ', released_year) AS summary FROM books ORDER BY released_year DESC LIMIT 3;

SELECT title, author_lname FROM books WHERE author_lname LIKE '% %';
 
SELECT title, released_year, stock_quantity FROM books ORDER BY stock_quantity LIMIT 3;
 
SELECT title, author_lname FROM books ORDER BY author_lname, title;
 
SELECT title, author_lname FROM books ORDER BY 2,1;
 
SELECT CONCAT('MY FAVORITE AUTHOR IS ', UPPER(author_fname),' ', UPPER(author_lname), '!' ) AS yell FROM books ORDER BY author_lname;

select count(*) as Book_Count from books; 
select 100/count(*) as data from books;  

SELECT COUNT(*) FROM books;
SELECT COUNT(author_lname) FROM books;
SELECT COUNT(DISTINCT author_lname) FROM books;
SELECT COUNT(*) FROM books WHERE title LIKE '%the%';

SELECT author_lname, COUNT(*) FROM books GROUP BY author_lname;
SELECT author_lname, COUNT(*) AS books_written FROM books GROUP BY author_lname ORDER BY books_written DESC;

SELECT MAX(pages) FROM books;
SELECT MIN(author_lname) FROM books;
SELECT title, pages FROM books WHERE pages = (SELECT MAX(pages) FROM books);
SELECT MIN(released_year) FROM books;
SELECT title, released_year FROM books WHERE released_year = (SELECT MIN(released_year) FROM books);

select * from books where pages=(select Max(pages) from books where title like '%Amazing%');

SELECT title, pages FROM books WHERE pages = (SELECT MAX(pages) FROM books);
 
SELECT MIN(released_year) FROM books;
 
SELECT title, released_year FROM books WHERE released_year = (SELECT MIN(released_year) FROM books);

SELECT author_fname, author_lname, COUNT(*) 
FROM books 
GROUP BY author_lname, author_fname;
 
 
SELECT CONCAT(author_fname, ' ', author_lname) AS author,  COUNT(*) FROM books GROUP BY author;
-- first book by author
SELECT author_lname, MIN(released_year) FROM books GROUP BY author_lname;
SELECT author_lname, MIN(released_year), MAX(released_year)FROM books GROUP BY author_lname;

SELECT author_lname, MAX(released_year), MIN(released_year) FROM books GROUP BY author_lname;
 
SELECT 
	author_lname, 
	COUNT(*) as books_written, 
	MAX(released_year) AS latest_release,
	MIN(released_year)  AS earliest_release,
      MAX(pages) AS longest_page_count
FROM books GROUP BY author_lname;
 
 
SELECT 
	author_lname, 
        author_fname,
	COUNT(*) as books_written, 
	MAX(released_year) AS latest_release,
	MIN(released_year)  AS earliest_release
FROM books GROUP BY author_lname, author_fname;

SELECT SUM(pages) FROM books;
SELECT author_lname, COUNT(*), SUM(pages) FROM books GROUP BY author_lname;

SELECT AVG(pages) FROM books;
SELECT AVG(released_year) FROM books;
select * from books;
SELECT released_year, AVG(stock_quantity), COUNT(*) FROM books GROUP BY released_year;
SELECT released_year AS year, COUNT(*) AS '# books', AVG(pages) AS 'avg pages' FROM books GROUP BY released_year ORDER BY released_year;

CREATE TABLE people (
	name VARCHAR(100),
    birthdate DATE,
    birthtime TIME,
    birthdt DATETIME
);
 
INSERT INTO people (name, birthdate, birthtime, birthdt)
VALUES ('Elton', '2000-12-25', '11:00:00', '2000-12-25 11:00:00');
 
INSERT INTO people (name, birthdate, birthtime, birthdt)
VALUES ('Lulu', '1985-04-11', '9:45:10', '1985-04-11 9:45:10');
 
INSERT INTO people (name, birthdate, birthtime, birthdt)
VALUES ('Juan', '2020-08-15', '23:59:00', '2020-08-15 23:59:00');

select * from people;
SELECT CURTIME() as CT;
SELECT CURDATE() as CD;
SELECT NOW() as today; 
select concat('-', NOW(), CURDATE(), CURTIME()) as time;
INSERT INTO people (name, birthdate, birthtime, birthdt)
VALUES ('Hazel', CURDATE(), CURTIME(), NOW());
SELECT birthdate, DAY(birthdate), DAYOFWEEK(birthdate), DAYOFYEAR(birthdate)FROM people;
SELECT  birthdate, MONTHNAME(birthdate), YEAR(birthdate) FROM people;

SELECT birthdate, DATE_FORMAT(birthdate, '%a %b %D') FROM people; 
SELECT birthdt, DATE_FORMAT(birthdt, '%H:%i') FROM people;
SELECT birthdt, DATE_FORMAT(birthdt, 'BORN ON: %r') FROM people;

CREATE TABLE captions (
  text VARCHAR(150),
  created_at TIMESTAMP default CURRENT_TIMESTAMP
);

INSERT into captions(text) values('hello');
select * from captions;
CREATE TABLE captions2 (
  text VARCHAR(150),
  created_at TIMESTAMP default CURRENT_TIMESTAMP,
  updated_at TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

INSERT into captions2(text) values('hello!');
select * from captions2;
update captions2 set text = "hello112"; 
select * from captions2;

SELECT CURTIME();
SELECT CURDATE();
SELECT DAYOFWEEK(CURDATE());
SELECT DAYOFWEEK(NOW());
SELECT DATE_FORMAT(NOW(), '%w') + 1;
SELECT DAYNAME(NOW());
SELECT DATE_FORMAT(NOW(), '%W');
SELECT DATE_FORMAT(CURDATE(), '%m/%d/%Y');
SELECT DATE_FORMAT(NOW(), '%M %D at %k:%i');
CREATE TABLE tweets(
    content VARCHAR(140),
    username VARCHAR(20),
    created_at TIMESTAMP DEFAULT NOW()
);
INSERT INTO tweets (content, username) VALUES('this is my first tweet', 'coltscat');
SELECT * FROM tweets;
INSERT INTO tweets (content, username) VALUES('this is my second tweet', 'coltscat');
SELECT * FROM tweets;


SELECT * FROM books
WHERE released_year != 2017;

SELECT * FROM books
WHERE title NOT LIKE '%e%';

SELECT * FROM books
WHERE released_year > 2005;
 
SELECT * FROM books
WHERE pages > 500;

SELECT * FROM books
WHERE pages < 200;
 
SELECT * FROM books
WHERE released_year < 2000;
 
SELECT * FROM books
WHERE released_year <= 1985;

SELECT title, author_lname, released_year FROM books
WHERE released_year > 2010
AND author_lname = 'Eggers';
 
SELECT title, author_lname, released_year FROM books
WHERE released_year > 2010
AND author_lname = 'Eggers'
AND title LIKE '%novel%';

SELECT title, pages FROM books 
WHERE CHAR_LENGTH(title) > 30
AND pages > 500;
 
SELECT title, author_lname FROM books
WHERE author_lname='Eggers' AND
released_year > 2010;
 
SELECT title, author_lname, released_year FROM books
WHERE author_lname='Eggers' OR
released_year > 2010;
 
 
SELECT title, pages FROM books
WHERE pages < 200 
OR title LIKE '%stories%';

SELECT title, released_year FROM books
WHERE released_year <= 2015
AND released_year >= 2004;

SELECT title, released_year FROM books
WHERE released_year BETWEEN 2004 AND 2014;

SELECT title, author_lname FROM books
WHERE author_lname = 'Carver' 
OR author_lname = 'Lahiri'
OR author_lname = 'Smith';
 
SELECT title, author_lname FROM books
WHERE author_lname IN ('Carver', 'Lahiri', 'Smith');
 
SELECT title, author_lname FROM books
WHERE author_lname NOT IN ('Carver', 'Lahiri', 'Smith');

SELECT title, released_year,
CASE
	WHEN released_year >= 2000 THEN 'modern lit'
    ELSE '20th century lit' 
END AS genre
FROM books;
 
 
SELECT 
    title,
    stock_quantity,
    CASE
        WHEN stock_quantity BETWEEN 0 AND 40 THEN '*'
        WHEN stock_quantity BETWEEN 41 AND 70 THEN '**'
        WHEN stock_quantity BETWEEN 71 AND 100 THEN '***'
        WHEN stock_quantity BETWEEN 101 AND 140 THEN '****'
        ELSE '*****'
    END AS stock
FROM
    books;
    
SELECT * FROM books WHERE released_year < 1980;
 
SELECT * FROM books 
WHERE author_lname = 'Eggers'
OR author_lname = 'Chabon';
 
SELECT * FROM books
WHERE author_lname = 'Lahiri'
AND released_year > 2000;
 
SELECT * FROM books
WHERE pages >= 100 
AND pages <= 200;
 
SELECT * FROM books
WHERE pages BETWEEN 100 and 200;
 
SELECT title, author_lname FROM books
WHERE author_lname LIKE 'C%'
OR author_lname LIKE 'S%';
 
SELECT title, author_lname
FROM books WHERE SUBSTR(author_lname, 1, 1) in ('C', 'S');
 
SELECT title, author_lname,
CASE
    WHEN title LIKE '%stories%' THEN 'Short Stories'
    WHEN title = 'Just Kids' THEN 'Memoir' 
    WHEN title = 'A Heartbreaking Work of Staggering Genius' THEN 'Memior'
    ELSE 'Novel'
END AS type
FROM books;
 
 
SELECT author_fname, author_lname,
	CASE
        WHEN COUNT(*) = 1 THEN '1 book'
        ELSE CONCAT(COUNT(*), ' books')
	END AS count
FROM books
WHERE author_lname IS NOT NULL
GROUP BY author_fname, author_lname;



CREATE TABLE contacts (
	name VARCHAR(100) NOT NULL,
    phone VARCHAR(15) NOT NULL UNIQUE
);
 
INSERT INTO contacts (name, phone)
VALUES ('billybob', '8781213455');
 
-- This insert would result in an error:
INSERT INTO contacts (name, phone)
VALUES ('billybob', '8781213455');

select * from contacts;


CREATE TABLE users (
	username VARCHAR(20) NOT NULL,
    age INT CHECK (age > 0)
);

insert into users (username, age) values('hello', 10);
insert into users (username, age) values('hello', -10); 
##08:56:46	insert into users (username, age) values('hello', -10)	Error Code: 3819. Check constraint 'users_chk_1' is violated.	0.000 sec
## Automaticaly given name users_chk_1

 select * from users;
 
CREATE TABLE palindromes (
  word VARCHAR(100) CHECK(REVERSE(word) = word)
);

INSERT into palindromes (word) values('hello');
INSERT into palindromes (word) values('ABA');
 select * from palindromes;
 
 ## Named age_not_negative
 CREATE TABLE users2 (
    username VARCHAR(20) NOT NULL,
    age INT,
    CONSTRAINT age_not_negative CHECK (age >= 0)
);
## 08:59:03	insert into users2 (username, age) values('hello', -10)	Error Code: 3819. Check constraint 'age_not_negative' is violated.	0.016 sec
insert into users2 (username, age) values('hello', -10); 

CREATE TABLE palindromes2 (
  word VARCHAR(100),
  CONSTRAINT word_is_palindrome CHECK(REVERSE(word) = word)
);


## Multiple column contraint
CREATE TABLE companies (
    name VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,
    CONSTRAINT name_address UNIQUE (name , address)
);
DESC companies;
insert into companies(name, address) values('A', 'A');
 
CREATE TABLE houses (
  purchase_price INT NOT NULL,
  sale_price INT NOT NULL,
  CONSTRAINT sprice_gt_pprice CHECK(sale_price >= purchase_price)
);

ALTER TABLE companies 
ADD COLUMN phone VARCHAR(15);## Null
 
ALTER TABLE companies
ADD COLUMN employee_count INT NOT NULL DEFAULT 1;## 1 if you remove default then default valye of data type like INT 0

DESC companies;
ALTER TABLE companies DROP COLUMN phone;

RENAME TABLE companies to suppliers;
ALTER TABLE suppliers RENAME TO companies;
DESC suppliers;

ALTER TABLE companies
RENAME COLUMN name TO company_name;



ALTER TABLE companies
MODIFY company_name VARCHAR(100) DEFAULT 'unknown';


ALTER TABLE suppliers
CHANGE business biz_name VARCHAR(50);

## CONSTAINT ADD or DROP
ALTER TABLE houses 
ADD CONSTRAINT positive_pprice CHECK (purchase_price >= 0);
ALTER TABLE houses DROP CONSTRAINT positive_pprice;

## Relation ships and practice 

CREATE TABLE customers (
    id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(50)
);
 
CREATE TABLE orders (
    id INT PRIMARY KEY AUTO_INCREMENT,
    order_date DATE,
    amount DECIMAL(8,2),
    customer_id INT,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);
 
INSERT INTO customers (first_name, last_name, email) 
VALUES ('Boy', 'George', 'george@gmail.com'),
       ('George', 'Michael', 'gm@gmail.com'),
       ('David', 'Bowie', 'david@gmail.com'),
       ('Blue', 'Steele', 'blue@gmail.com'),
       ('Bette', 'Davis', 'bette@aol.com');
       
       
INSERT INTO orders (order_date, amount, customer_id)
VALUES ('2016-02-10', 99.99, 1),
       ('2017-11-11', 35.50, 1),
       ('2014-12-12', 800.67, 2),
       ('2015-01-03', 12.50, 2),
       ('1999-04-11', 450.25, 5);
       
select * from customers;
select * from orders;
##07:52:06	insert into orders (order_date, amount, customer_id) values('2024-02-02', 10.19, 22)	Error Code: 1452. Cannot add or update a child row: a foreign key constraint fails (`book_store`.`orders`, CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`))	0.000 sec
insert into orders (order_date, amount, customer_id) values('2024-02-02', 10.19, 22);

select o.amount, c.first_name from orders o, customers c where c.id = o.customer_id AND o.order_date = '1999-04-11';
SELECT id FROM customers WHERE last_name = 'George';
SELECT * FROM orders WHERE customer_id = 1;

SELECT * FROM orders 
WHERE customer_id = (SELECT id FROM customers WHERE last_name = 'George');

-- To perform a (kind of useless) cross join/Cartesian product :
SELECT * FROM customers, orders;

-- To perform a  inner join: No Need to specify the key woek INNER its Optional
-- Our first inner join!
SELECT * FROM customers
JOIN orders ON orders.customer_id = customers.id;

##OR
SELECT * FROM customers
INNER JOIN orders ON orders.customer_id = customers.id;
 
SELECT first_name, last_name, order_date, amount FROM customers
JOIN orders ON orders.customer_id = customers.id;

##OR
SELECT first_name, last_name, order_date, amount FROM customers
INNER JOIN orders ON orders.customer_id = customers.id;
 
-- The order doesn't matter here:
SELECT * FROM orders
JOIN customers ON customers.id = orders.customer_id;

-- Or
SELECT * FROM orders
INNER JOIN customers ON customers.id = orders.customer_id;

SELECT 
    first_name, last_name, SUM(amount) AS total
FROM
    customers
        JOIN
    orders ON orders.customer_id = customers.id
GROUP BY first_name , last_name
ORDER BY total;

SELECT 
    customers.id, first_name, last_name, SUM(amount) AS total
FROM
    customers
        JOIN
    orders ON orders.customer_id = customers.id
GROUP BY customers.id
ORDER BY total;

SELECT 
    first_name, last_name, order_date, amount
FROM
    customers
        LEFT JOIN
    orders ON orders.customer_id = customers.id;
 
 
SELECT 
    order_date, amount, first_name, last_name
FROM
    orders
        LEFT JOIN
    customers ON orders.customer_id = customers.id;

## Handle null
SELECT 
    first_name, last_name, order_date, amount
FROM
    customers
        LEFT JOIN
    orders ON orders.customer_id = customers.id;
    
SELECT 
    first_name, 
    last_name, 
    IFNULL(SUM(amount), 0) AS money_spent
FROM
    customers
        LEFT JOIN
    orders ON customers.id = orders.customer_id
GROUP BY first_name , last_name;
  
SELECT 
    first_name, 
    last_name, 
    IFNULL(SUM(amount), 0) AS money_spent
FROM
    customers
        LEFT JOIN
    orders ON customers.id = orders.customer_id
GROUP BY first_name , last_name
order by money_spent ASC;

SELECT 
    first_name, last_name, order_date, amount
FROM
    customers
        RIGHT JOIN
    orders ON customers.id = orders.customer_id;
    
    
## Delete casecade 
DROP table orders;
DROP table customers;
select * from customers;

CREATE TABLE customers (
    id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(50)
);
 
CREATE TABLE orders (
    id INT PRIMARY KEY AUTO_INCREMENT,
    order_date DATE,
    amount DECIMAL(8 , 2 ),
    customer_id INT,
    FOREIGN KEY (customer_id)
        REFERENCES customers (id)
        ON DELETE CASCADE
);

INSERT INTO customers (first_name, last_name, email) 
VALUES ('Boy', 'George', 'george@gmail.com'),
       ('George', 'Michael', 'gm@gmail.com'),
       ('David', 'Bowie', 'david@gmail.com'),
       ('Blue', 'Steele', 'blue@gmail.com'),
       ('Bette', 'Davis', 'bette@aol.com');
       
       
INSERT INTO orders (order_date, amount, customer_id)
VALUES ('2016-02-10', 99.99, 1),
       ('2017-11-11', 35.50, 1),
       ('2014-12-12', 800.67, 2),
       ('2015-01-03', 12.50, 2),
       ('1999-04-11', 450.25, 5);

select * from customers;
select * from orders;
delete from customers where last_name='Michael';


## More practice

CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50)
);
 
CREATE TABLE papers (
    title VARCHAR(50),
    grade INT,
    student_id INT,
    FOREIGN KEY (student_id)
        REFERENCES students (id)
);

INSERT INTO students (first_name) VALUES 
('Caleb'), ('Samantha'), ('Raj'), ('Carlos'), ('Lisa');
 
INSERT INTO papers (student_id, title, grade ) VALUES
(1, 'My First Book Report', 60),
(1, 'My Second Book Report', 75),
(2, 'Russian Lit Through The Ages', 94),
(2, 'De Montaigne and The Art of The Essay', 98),
(4, 'Borges and Magical Realism', 89);
 
SELECT 
    first_name, title, grade
FROM
    students
        JOIN
    papers ON papers.student_id = students.id
ORDER BY grade DESC;
 
SELECT 
    first_name, title, grade
FROM
    students
        LEFT JOIN
    papers ON papers.student_id = students.id;
 
SELECT 
    first_name, IFNULL(title, 'MISSING'), IFNULL(grade, 0)
FROM
    students
        LEFT JOIN
    papers ON papers.student_id = students.id;
  
SELECT 
    first_name, IFNULL(AVG(grade), 0) AS average
FROM
    students
        LEFT JOIN
    papers ON students.id = papers.student_id
GROUP BY first_name
ORDER BY average DESC;
 
SELECT 
    first_name,
    IFNULL(AVG(grade), 0) AS average,
    CASE
        WHEN IFNULL(AVG(grade), 0) >= 75 THEN 'passing'
        ELSE 'failing'
    END AS passing_status
FROM
    students
        LEFT JOIN
    papers ON students.id = papers.student_id
GROUP BY first_name
ORDER BY average DESC;
##

```

