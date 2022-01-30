# Sorting a list of dictionary elements
# Description
# A teacher decided to divide the class into groups to conduct fun activities. Each group had one or more members in it. The data is provided in the form of a list with dictionary elements. The key and value in each dictionary correspond to the student’s roll number and his/her name.
# In case the length of two or more dictionaries are the same, then the dictionary that occurs first in the input list will also appear first among the other dictionaries of the same length.
# Your task is to write a Python program to sort the list in descending order with respect to the group strength.﻿
# Note: Use lambda and sorted functions to solve the question.
# Input: List
# Output: List
# ----------------------------------------------------------------------
# Sample input: [{4: 'Viking', 9: 'Happy', 10: 'Tony', 2: 'Rogers'}, {12: 'Vikram', 19: 'Vipan'}, {3: 'Kohli'}, {1: 'Ronaldo', 29: 'Harish', 7: 'Ganesh'}]
# Sample output: [{4: 'Viking', 9: 'Happy', 10: 'Tony', 2: 'Rogers'}, {1: 'Ronaldo', 29: 'Harish', 7: 'Ganesh'}, {12: 'Vikram', 19: 'Vipan'}, {3: 'Kohli'}]
# ----------------------------------------------------------------------
# Sample input: [{14: 'Darpan', 19: 'Harry', 10: 'Julia'}, {12: 'Ethan', 19: 'Rogers'}, {3: 'Kohli', 1: 'Neymar', 29: 'Sachin', 7: 'Ramesh'}]
# Sample output: [{3: 'Kohli', 1: 'Neymar', 29: 'Sachin', 7: 'Ramesh'}, {14: 'Darpan', 19: 'Harry', 10: 'Julia'}, {12: 'Ethan', 19: 'Rogers'}]
# ----------------------------------------------------------------------
#take input here using ast sys
import ast
l1 = ast.literal_eval(input())

def sortt(key):
    return len(key.keys())
    
print(sorted(l1, key=sortt, reverse=True))