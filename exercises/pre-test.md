---
layout: exercise
title: CS 2316 Pre-test
---

# CS 2316 Pre-test

## Introduction

In order to accommodate the ISyE department's request for additional material on data analytics, CS 2316 will require incoming students to have a basic proficiency in Python or the ability to get up to speed quickly with Python. The following exercises are designed to help you gauge your own readiness for CS 2316. If you can figure out these exercises by the end of the first week of the semester you will have no problem in the course. If you find them difficult but manageable then you'll probably be fine because we will review Python in the first three weeks. If you have no idea how to begin these exercises, you should drop CS 2316 and improve your Python programming skills before registering again.

## Exercises

We expect that you will use loops in these exercises, but within the first three weeks of CS 2316 you will be able solve each of these exercises with one line of Python code.

1. Write a function called `contains` that takes a list of numbers and a query number and returns `True` if the list contains the query number, `False` otherwise.  You will need a loop, your loop must not execute more iterations than necessary, and you cannot use `break` or `continue` or the `in` operator.

2. Write a function called `num_evens` that takes a list of numbers and returns the number of even numbers in the list.

3. Given a `list[list[str]]` of student grades where the first list is a header and subsequent lists have a name followed by grades such as the following:

```Python
super_grades = [
    # First line is descriptive header. Subsequent lines hold data
    ['Student', 'Exam 1', 'Exam 2', 'Exam 3'],
    ['Thorny', '100', '90', '80'],
    ['Mac', '88', '99', '111'],
    ['Farva', '45', '56', '67'],
    ['Rabbit', '59', '61', '67'],
    ['Ursula', '73', '79', '83'],
    ['Foster', '89', '97', '101']
]
```

Write a Python script that prints:

- each student's name followed by their average score, and
- the name of each graded item with the average score for that item.
