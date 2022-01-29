# List comprehension

number = [1,2,3,4,5,6]
"""
Instead of using for loop to add 1 number to every number in the lis we use lis comprehension
"""

new_number = [n+1 for n in number]
print(number)

# List comprehensions work witth strings also
name = "Aryan"
letters = [letter for letter in name]
print(letters)

# Using list comprehension in range
range_list = [number*2 for number in range(1, 5)]
print(range_list)

# Conditional list comprehension
names = ["Aryan", "Shubham", "Anushka", "Vivek", "Shrriya"]
short_names = [name.upper() for name in names if len(name) == 5]
print(short_names)

# Dictionary comprehension

# dict = {key_name: key_value for item in _____ }

names = ["Aryan", "Vivek", "Anushka"]
import random
names_score = {students: random.randint(1, 100) for students in names}
print(names_score)

# Looping into a dictionary using dictionary comprehension

passed = {student: score for (student, score) in names_score.items() if score > 60}
print(passed)

