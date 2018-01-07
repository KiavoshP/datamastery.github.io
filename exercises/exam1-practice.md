---
layout: exercise
title: CS 2316 - Exam 1 Pratice
---

# Exam 1 Practice


- Write an expression that takes the string `"Thorny,Farva,Mac,Rabbit,Foster"` and returns the list  `["Thorny", "Farva", "Mac", "Rabbit", "Foster"]`.

- Write an expression that takes list `["Thorny", "Farva", "Mac", "Rabbit", "Foster"]` and returns the string `"Thorny and Farva and Mac and Rabbit and Foster"`.

- Write a single expression that takes the string `"Thorny and Farva and Mac and Rabbit and Foster"` and returns the string with the `and`s replaced by `et`s.

- Write a single expression that takes the list `["Thorny", "Farva", "Mac", "Rabbit", "Foster", "Farva"]` and returns a data structure with no duplicate elements.

- Write a Python script named `calc.py` that takes three command line arguments, where the first command line argument is a number (first operand), the second is an arithmentic operator, and the third is a number (second operand). When run, your program should print the result of applying the operator to the operands. For example:

```sh
$ python calc.py 1 + 2
3
```

Your program should support at least the operators `+`, `-`, `*`, `/`.

- Write a single expression that takes a list of strings like `["Germany:Berlin", "France:Paris", "England:London"]` and returns a dictionary like  `{'Germany': 'Berlin', 'France': 'Paris', 'England': 'London'}`

- Assuming `emails = ["abdallah@hotmail.com", "bob@aol.com", "chen@gmail.com",  "dhruv@aol.com"]` has been executed, replace the following snippet of code with a single line that uses a list comprehension, filling in CONDITION with an expression that evaluates to `True` if the email is an `aol.com` email address.

```Python
retro_chic = []
for e in emails:
    if CONDITION:
        retro_chic.append(e)
```
