---
layout: homework
title: Homework 4 - MARTA Database
---

# Homework 4 MARTA Database


## Introduction

In this assignment you'll practice writing to and reading from databases in Python.


## General Instructions

**This is an individual assignment.**

Collaboration at a reasonable level will not result in substantially similar code. Students may only collaborate with fellow students currently taking this course, the TA's and the lecturer. Collaboration means talking through problems, assisting with debugging, explaining a concept, etc. You should not exchange code or write code for others.

Notes:

- Include a comment with your name, Canvas ID and GTID at the top of all Python files.
- *Do not wait until the last minute* to do this assignment in case you run into problems.
- Pay close attention to whether problems require you to print or return the results! Printing instead of returning or vice versa will result in a point deduction.
- Name all functions as specified in the instructions.
- Unless otherwise stated, you can assume inputs will be valid in this assignment (i.e. error checking is not required).
- In a Python module you must define a value (such as a function) before referencing it. So if you call function A from function B, the definition of function A must come before the definition of function B in the file.


## Problem Description

MARTA is considering some new projects that they want to undertake to improve their service and connectivity in the Atlanta area. They’ve hired you to analyze their data and give them valuable insight that will help them make the best investment.

As they are not the best at keeping their data well organized, they have sent you the data in the form of a csv file (example: [passenger_data.csv](passenger_data.csv)). Since this file contains too many rows of data to process efficiently using the csv module, you are going to enter this data into a database and then query it to analyze the data.


## Solution Description

Create a database to make it convenient to answer certain kinds of questions and import data into that database.

### Part 1 - Create the database schema

-	Write a database creation script called `marta-schema.sql` that creates a database called `marta` with create table statements that create the following tables

	- `routes` with fields:
		- `route_id` as the primary key
		- `route_name`
	- `stops` with fields:
		- `stop_id` as the primary key
		- `stop_name`
	- `vehicles` with fields:
		- `vehicle_id` as the primary key
	- `passenger_data` with fields:
		- `index` as the primary key
		- `date`
		- `route_id` as a foreign key referencing route_id in routes
		- `direction`
		- `stop_id` as a foreign key referencing stop_id in stops
		- `on_number` the number of people that got on the train (or 0 if there is no data)
		- `off_number` the number of people that got off the train (or 0 if there is  data)
		- `vehicle_id` as a foreign key referencing vehicle_id in vehicles


### Part 2 - Populate the database

- Write a python script called `import_marta.py` that reads in the given csv file and stores the information from the appropriate columns of the csv file into the appropriate table(s) of the database, which you can assume has already been created using your `marta-schema.sql` script.

- The name of the csv file and the database will be passed in as command line arguments to your program. **Do not hard code the name of the csv file or the database.** Your program must be able to read from the csv file whose name is given as the first command line argument and write to the database whose name is given in the second command line argument

- Your program will be run in the following manner:

```sh
$ python import_marta.py passenger_data.csv marta localhost root
Password for root@localhost:
Importing data from passenger_data.csv into marta database on localhost...
Done.
```

Don't print the `Done.` line until the import is complete.

### Part 3 - Queries

In a file `marta-queries.sql`, write SQL queries to answer each of the following questions:
-	What is the `stop_name` where the most people got on? What is the `stop_name` where the most people got off? (Hint: You will need to use an aggregate function)
-	What is the `vehicle_id` of the vehicle that made the most number of stops  (not necessarily unique)?
-	What is the `vehicle_id` of the vehicle that visited the least number of unique stops in the given period?
-	What is the `stop_name` of the stop that is visited along the greatest number of unique routes?
-	Which `direction` has the highest passenger traffic? (Passenger traffic is determined by the sum of the number of people getting on at any stop along a route in a given direction)  Which `direction` has the lowest?
-	What is the `route_name` of the most popular route? (The most popular route is the one with the highest average passenger traffic in either direction)
-	You are given data for Friday – Tuesday (7/1/2016 – 7/5/2016). Which `date` has the highest passenger traffic and which date has the lowest?

### Tips and Considerations

- Use the [getpass](https://docs.python.org/3/library/getpass.html) module for getting an password from the terminal without echoing it. For example:

  ```
  import getpass
  pw = getpass.getpass("Password: ")
  Password: **** (or some other means of hiding the text used on your terminal)
  ```

- https://datamastery.github.io/slides/python-db-api.pdf

## Grading

- 25 points for creating the database schema correctly
- 25 points for populating the database correctly
- 50 points for answering the questions using correct SQL queries


## Turn-in Procedure

Submit your `marta-schema.sql`, `import_marta.py` and `marta-queries.sql` files on Canvas. After you turn in your files, make sure to check that you have submitted the correct files that you intended to. It is highly recommended that you submit the assignment early and often in order to avoid incorrect/incomplete submissions near the deadline.

Good luck!
