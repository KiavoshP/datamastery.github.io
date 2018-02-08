---
layout: homework
title: Homework 2 - Practice
---

# Homework 2 - `practice` Module

## Introduction

In this assignment you'll practice manipulating data structures in Python.

## General Instructions

**This is an individual assignment.**

Collaboration at a reasonable level will not result in substantially similar code. Students may only collaborate with fellow students currently taking this course, the TA's and the lecturer. Collaboration means talking through problems, assisting with debugging, explaining a concept, etc. You should not exchange code or write code for others.

Notes:

- Include a comment with your name, Canvas login ID, and GTID at the top of all Python files.
- *Do not wait until the last minute* to do this assignment in case you run into problems.
- Pay close attention to whether problems require you to print or return the results! Printing instead of returning or vice versa will result in a point deduction.
- Name all functions as specified in the instructions.
- Unless otherwise stated, you can assume inputs will be valid in this assignment (i.e. error checking is not required).
- In a Python module you must define a value (such as a function) before referencing it. So if you call function A from function B, the definition of function A must come before the definition of function B in the file.


## Problem Description

You have an exam soon and you want to practice for the exam.

## Solution Description

Write a module named `practice` which imports a module called `practice_data` with the elements in this example [practice_data](practice_data.py). We suggest using `from practice_data import *` for convenience.

Your `practice` module should define the following variables using the data from `practice_data`:

- `e2f` -- a dictionary mapping English words to French words built from the lists `en` and `fr` in [practice_data](practice_data.py). The English and French words correspond positionally, that is, the first word in `fr` is the French translation of the first word in `en`, and so on. Using the data in [practice_data](practice_data.py) your `e2f` would look something like:

  ```Python
  {'good bye': 'au revoir',
   'hello': 'bonjour',
   'to be': 'être',
   'to have': 'avoir',
   'to lose': 'perdre',
   'to love': 'aimer',
   'to practice': "s'entraîner",
   'to win': 'gagner'}
  ```

- `e2both` -- a dictionary mapping English words to dictionaries mapping `'fr'` to the corresponding French word, and `'de'` to the corresponding German word. Using the data in [practice_data](practice_data.py) your `e2both` would look something like:

  ```Python
  {'good bye': {'de': 'auf wiedersehen', 'fr': 'au revoir'},
   'hello': {'de': 'guten tag', 'fr': 'bonjour'},
   'to be': {'de': 'sein', 'fr': 'être'},
   'to have': {'de': 'haben', 'fr': 'avoir'},
   'to lose': {'de': 'verlieren', 'fr': 'perdre'},
   'to love': {'de': 'lieben', 'fr': 'aimer'},
   'to practice': {'de': 'üben', 'fr': "s'entraîner"},
   'to win': {'de': 'gewinnen', 'fr': 'gagner'}}
  ```

- `love_de` -- the German word for love, from the `e2both` dictionary you created above.

- `avoir_en` -- the English word for the French "avoir", taken from the `e2f` you created above. Note that this is the only part of this assignment that can't be done in one line. You'll be using a value to find its corresponding key.

- `location2temps` - a dictionary mapping locations to lists of water temperatures from the `water_temps` variable in [practice_data](practice_data.py). Should look something like:

  ```Python
  {'Cape Hatteras NC': [49, 46, 52, 65, 72, 78, 81, 81, 79, 71, 58, 55],
   'Charleston SC': [50, 50, 57, 65, 72, 78, 81, 81, 79, 71, 63, 54],
   'Chesapeake Bay VA': [46, 42, 44, 65, 72, 78, 81, 81, 79, 71, 56, 49],
   'Daytona Beach FL': [61, 59, 65, 65, 72, 78, 81, 81, 79, 71, 71, 65],
   'Duck NC': [45, 44, 46, 65, 72, 78, 81, 81, 79, 71, 59, 52],
   'Fernandina Beach FL': [55, 55, 62, 65, 72, 78, 81, 81, 79, 71, 66, 58],
   'Kiptopeke VA': [36, 39, 46, 65, 72, 78, 81, 81, 79, 71, 54, 44],
   'Lewisetta VA': [39, 40, 48, 65, 72, 78, 81, 81, 79, 71, 53, 44],
   'Mayport FL': [58, 58, 62, 65, 72, 78, 81, 81, 79, 71, 69, 62],
   'Miami Beach FL': [71, 73, 75, 65, 72, 78, 81, 81, 79, 71, 76, 73],
   'Money Point VA': [49, 49, 55, 65, 72, 78, 81, 81, 79, 71, 60, 54],
   'Myrtle Beach SC': [48, 50, 55, 65, 72, 78, 81, 81, 79, 71, 61, 53],
   'Savannah Beach GA': [51, 52, 59, 65, 72, 78, 81, 81, 79, 71, 64, 54],
   'St Augustine Beach FL': [57, 56, 61, 65, 72, 78, 81, 81, 79, 71, 67, 60],
   'Stuart Beach FL': [67, 66, 70, 65, 72, 78, 81, 81, 79, 71, 75, 70],
   'Virginia Beach VA': [55, 53, 48, 65, 72, 78, 81, 81, 79, 71, 60, 60],
   'Virginia Key FL': [71, 72, 74, 65, 72, 78, 81, 81, 79, 71, 76, 73],
   'Wilmington NC': [58, 58, 62, 65, 72, 78, 81, 81, 79, 71, 69, 62],
   'Yorktown VA': [42, 42, 49, 65, 72, 78, 81, 81, 79, 71, 56, 47]}
  ```

- `min_miami_temp` -- use the `min` function and `location2temps` to assign to this variable the minimum monthly temperature in Miami Beach FL.

- `avg_location_temps` -- a dictionary mapping locations from `water_temps` to their average temperature for all months. Should look something like:

  ```Python
  {'Cape Hatteras NC': 65.58333333333333,
   'Charleston SC': 66.75,
   'Chesapeake Bay VA': 63.666666666666664,
   'Daytona Beach FL': 70.66666666666667,
   'Duck NC': 64.41666666666667,
   'Fernandina Beach FL': 68.58333333333333,
   'Kiptopeke VA': 62.166666666666664,
   'Lewisetta VA': 62.583333333333336,
   'Mayport FL': 69.66666666666667,
   'Miami Beach FL': 74.58333333333333,
   'Money Point VA': 66.16666666666667,
   'Myrtle Beach SC': 66.16666666666667,
   'Savannah Beach GA': 67.25,
   'St Augustine Beach FL': 69,
   'Stuart Beach FL': 72.91666666666667,
   'Virginia Beach VA': 66.91666666666667,
   'Virginia Key FL': 74.41666666666667,
   'Wilmington NC': 69.66666666666667,
   'Yorktown VA': 63.583333333333336}
 ```

- `warmest_location` use `avg_location_temps` and the `max` function to assign to this variable the location with the warmest average temperature.


- `avg_month_temps` -- a dictionary mapping months to the average temperature for that month across all locations. Should look something like:

  ```Python
  {'APR': 65,
   'AUG': 81,
   'DEC': 57.31578947368421,
   'FEB': 52.8421052631579,
   'JAN': 53.05263157894737,
   'JUL': 81,
   'JUN': 78,
   'MAR': 57.36842105263158,
   'MAY': 72,
   'NOV': 63.8421052631579,
   'OCT': 71,
   'SEP': 79}
  ```

- `warmest_month` -- use `avg_month_temps` and the `max` function to assign to this variable the name of the month with the warmest average temperature.


## Grading

- 10 points for each item listed above.

## Turn-in Procedure

Submit your `practice.py` file on Canvas as an attachment.  When you're ready, double-check that you have submitted and not just saved a draft.
