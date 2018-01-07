---
layout: exercise
title: Student Class Exercise
---

# Student Class Exercise

## Introduction

In this exercise you will practice

- writing and using simple Python classes,
- writing and using simple enums, and
- using data structures with objects.

## Problem Description

You need to manage a database of students.

## Solution Description

Write a Python module in a file named `student.py` with the following definitions:

- A `Major` [enum](https://docs.python.org/3/library/enum.html) that defines available college majors and thier relative "order".
- A `Student` class with instance variables `name`, `year`, and `major`. `Student` should have an `__init__()` method that allows construction of a complete `Student` instance at initialization time, such as `stud = Student("Robert Paulson", 3, Major.IE)`
- Write a `__lt__()` method for `Student` that defines the way students are ordered.
- Write ...