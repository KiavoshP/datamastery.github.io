---
layout: homework
title: Homework 3 - Interns
---

# Homework 3 - Interns

## Introduction

In this homework you will practice

- reading data from CSV files,
- reading data from JSON files, and
- using classes and objects.

## General Instructions

**This is an individual assignment.**

Collaboration at a reasonable level will not result in substantially similar code. Students may only collaborate with fellow students currently taking CS 2316, the TAs and the lecturer. Collaboration means talking through problems, assisting with debugging, explaining a concept, etc. You should not exchange code or write code for others.

Notes:

- Include a comment with your name and canvasID at the top of all Python files.
- *Do not wait until the last minute* to do this assignment in case you run into problems.
- Pay close attention to whether problems require you to print or return the results! Printing instead of returning or vice versa will result in a point deduction.
- Name all functions as specified in the instructions.
- Unless otherwise stated, you can assume inputs will be valid in this assignment (i.e. error checking is not required).
- In a Python module you must define a value (such as a function) before referencing it. So if you call function A from function B, the definition of function A must come before the definition of function B in the file.

## Problem Description

Congrats! You are the Supply Chain Manager at a major company, and you're tasked with deciding your intern team for the Summer. Luckily, HR has summarized applicant data for you, and your job is to decide whom to hire and their offer details.

## Solution Description

HR provies you with CSV and JSON files containing candidate information:

- A CSV file of academic records with candidate names, IDs, email addresses, completed semester hours, GPA, and grade in CS 2316, if they took CS 2316. Sample: [academics.csv](academics.csv)

- A JSON dictionary mapping candidate IDs to their interview scores, where interview scores are represents as 2-element lists where the first element is the technical interview score and the second is the behavioral interview score. Sample: [interviews.json](interviews.json)

Create a module called `interns` that reads these data files and generates rankings of candidates for use in hiring decisions. Your module should define a `Candidate` class which includes/overrides the following methods:

- a `__init__` method which take parameters that initialize the following instance variables:

  - `id` -- a unique identifier for the student
  - `name` -- the student's name
  - `gpa` -- the cumulative GPA of the student
  - `cs2316grade` -- the grade the student earned in CS 2316, e.g., `'A'`, `'B'`, etc., or `None` if the student didn't take CS 2316
  - `technical_interview` -- the student's technical interview score
  - `behavioral_interview` -- the student's behavioral interview score

- a magic method that prodcues a string representation of a `Candidate` instance when an instance is printed or when an instance's value is echoed in an interactive Python interpreter. The string representation should include the candidate's id and name, e.g. `rfarva3 - Rodney Farva`.
- a magic method that, when instances of `Candidate` are sorted, produces an ordering based on a composite score calcualted by `gpa` + `technical_interview` + `behavioral_interview` + CS 23126 grade point, where grade point is 4 for A, 3 for B, etc. For example, a student with a 3.0 GPA, 10 techincal intervew and 10 behavioral interview and a B in CS 2316 would have a composite score of 3.0 + 10 + 10 + 3 = 26.

In addition to the `Candidate` class, include the following functions:

- `rank_composite(candidates)` which takes a list of candidates and returns another list with the same elements but sorted in descending order by the composite score described for the "makes Candidate instances sortable" magic method described above.

- `rank_academics(candidates)` which takes a list of candidates and returns another list with the same elements but sorted in descending order by `gpa` + CS 2316 grade point. For example, a candidate with a 3.2 GPA and an A in CS 2316 (4.0 CS 2316 grade point) would be ranked above a candidate with a 4.0 GPA and a B in CS 2316.

- `rank_technical_interview(candidates)` which takes a list of candidates and returns another list with the same elements but sorted in descending order by the candidates' techincal interview scores.

- `rank_behavioral_interview(candidates)` which takes a list of candidates and returns another list with the same elements but sorted in descending order by the candidates' behavioral interview scores.

When the `interns` module is imported as a script it should only make the class and function definitions described above. When the `interns` module is run as a script it should take two mandatory and one optional command line arguments. The first command line argument is the name of a CSV file organized exactly like [academics.csv](academics.csv), the second command line argument is the name of a file organized exactly like [interviews.json](interviews.json), and the third (optional) command line argument is a ranking criterion. The interviews JSON file should contain interview scores for all the students in the academics CSV file. When the script is run without the third command line argument, the students are printed in order as ranked by their composite scores. If the third command line argument is given, it should specify one of the other rank orders from the module functions listed above: academics, technical_interview, or behavioral_interview. If the user supplies a third command line argument that is not one of the specified rank order options, print the students ranked by composite score.

Example script runs:

```sh

```

## Grading

Candidate Class - 50 Points
- init: 5 Points for instantiating variables correctly
- repr: 5 Points for a string representation of the object
- eq: 5 points for testing equality
- gt: 5 points for correct implementation
- calcExperience : 15 points for correct implementation
- calcInterview : 15 points for correct implementation


## Submission Instructions

Attach your `interns.py` file to your Canvas HW2 assignment submission.

Practice safe submission! Verify that your HW files were truly submitted correctly, the upload was successful, and that your program runs with no syntax or runtime errors. It is solely your responsibility to turn in your homework and practice this safe submission safeguard.
