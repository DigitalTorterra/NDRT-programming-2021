"""
Week 1, Challenge 2

Write a program to find the sum of the first "n" natural numbers.

Tools:
- basic operators and variables
- if/elif/else statements
- while loops

Fun fact: you can also use the formula n(n+1)/2
"""

# Control variables
n = 100

# While loop
total = 0
i = 0
while i <= n:
    total = total + i
    i = i + 1

# Cheap trick
total_cheap = int(n*(n+1)/2)

print(f'The sum of the first {n} numbers is {total}, which is also {total_cheap}')
