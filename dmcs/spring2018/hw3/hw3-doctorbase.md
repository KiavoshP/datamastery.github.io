---
layout: homework
name: Doctorbase
---

# Doctorbase

## Introduction


A common task in data management systems is receiving data from an external system in XML, JSON, or CSV files and storing it in a relational database. Python includes libraries for easily reading these files and interacting with databases. We store data in databases for record keeping and so that we can answer questions about the data.

In this assignment you will

-   create a database,

-   write a Python program that parses input data files and inserts the
    data from them into the database, and

-   create a SQL script with queries to answer questions about data in
    the database.

## Problem Description


You’re starting a new job as a database manager at the Centers for Disease Control (CDC). In this role you need to manage and analyze data about doctors and patient care. You receive doctor data from outside sources in the form of XML, CSV and JSON files which you need to insert into your database, and you use the database to answer questions about the data.

## Solution Description

Create a database to store the data and write a Python script to import data from files and insert them into the database.

### Create your database

Design a database to track doctors, patients, and doctor visits.

- For doctors track first name, last name, and specialty.
- For patients track first name, last name, and primary care provider (which is a doctor).
- For visits track the doctor, patient, and date and time of visit

You may assume:

- A doctor may have many patients
- A patient will have only one primary care provider
- Doctors are never patients

Write a SQL script, `doctors-schema.sql`, that creates your database schema in a database called `doctors`.

### Import data into your database

Write a Python script named `import_doctors.py` that takes three command-line arguments:

- an XML file containing doctor information (example: [doctors.xml](doctors.xml)),
- a CSV files containing patient information (example: [patients.csv](patients.csv)), and
- a JSON file containing visit information (example: [visits.json](visits.json)).

Your script should insert information from the files above into the appropriate tables in the database with apppropriate key and foreign key values.

### Query your database

Write a SQL script, `doctors-queries.sql`, that includes queries to answer the following questions:

-   What are the first names and last names of the patients who have cardiologists for primary care providers (PCP)?

-   What are the first names and last names of the patients who saw their doctor (PCP) in May 2010?

-   OPTIONAL BONUS (5 points): What are the first name and last name of the doctor who has the most patients (not the most visits)?

-   OPTIONAL BONUS (5 points): What are the first names and last names of the doctors who have no patients (not visits)?

Your `doctors-queries.sql` should contain only the `SELECT` queries requested above.

## Turn-in Procedure

Submit your `doctors-schema.sql`, `import_doctors.py`, `doctors-queries.sql` to the assignment on Canvas as attachments. After you submit your files, download them from Canvas to an empty directory on your disk and double-check that they are the ones you intended to submit.
