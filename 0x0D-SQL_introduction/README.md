this project involves the use sql(Structured Query Language) with realtional database Mysql to work on some databased projects, involving learning of the language.

#TASK1:
Write a script that lists all databases of your MySQL server.

#TASK2:
Write a script that creates the database hbtn_0c_0 in your MySQL server.


#TASK3:
Write a script that deletes the database hbtn_0c_0 in your MySQL server.


#TASK4:
Write a script that lists all the tables of a database in your MySQL server.



TASK5:
Write a script that creates a table called first_table in the current database in your MySQL server.

#TASK6:
Write a script that prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server.

#TASK7:
Write a script that lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server.

#TASK8:
Write a script that inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server.

New row:
id = 89
name = Best School

#TASK9:
Write a script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server.

TASK10:
Write a script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.

second_table description:
id INT
name VARCHAR(256)
score INT
The database name will be passed as an argument to the mysql command
If the table second_table already exists, your script should not fail
You are not allowed to use the SELECT and SHOW statements
Your script should create these records:
id = 1, name = “John”, score = 10
id = 2, name = “Alex”, score = 3
id = 3, name = “Bob”, score = 14
id = 4, name = “George”, score = 8

#TASK11:
Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.

Results should display both the score and the name (in this order)
Records should be ordered by score (top first)
The database name will be passed as an argument of the mysql command

#TASK12:
Write a script that updates the score of Bob to 10 in the table second_table.

You are not allowed to use Bob’s id value, only the name field
The database name will be passed as an argument of the mysql command

#TASK13:
Write a script that removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in your MySQL server.

The database name will be passed as an argument of the mysql command