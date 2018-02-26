---
layout: exercise
title: quiz3
---

# quiz3

Write a module named `averages` that, when run as a script, reads student names and grades from a CSV file named in the first command-line argument to the script and saves a JSON file with a dictionary mapping the student names to their score averages. For example, given the CSV grades file [super-grades.csv](super-grades.csv), the following command line invocation

```
$ python averages.py super-grades.csv super-averages.json
```

would produce a JSON file named `super-averages.json` with the following contents (note that the order of the key-value mappings may differ and it won't necessarily be formatted nicely like this example):

```
{
 "Thorny": 90.0,
 "Mac": 99.33333333333333,
 "Farva": 56.0,
 "Rabbit": 62.333333333333336,
 "Ursula": 78.33333333333333,
 "Foster": 95.66666666666667
}
```

You may assume that your program will always get two command line arguments and that the grades CSV file will always contain only the student names and Exam 1, Exam 2, and Exam 3 as in the [super-grades.csv](super-grades.csv) example.

## Tips

- You may find the solution to the [grades module exercise](grades.html) helpful.
- You can probably go quicker if you just import `statistics` (for its `mean` function) and write it from scratch.
- Don't forget to convert strings to numberic types, like `float`, where necessary.
- Don't forget to import the `sys`, `csv`, and `json` modules.