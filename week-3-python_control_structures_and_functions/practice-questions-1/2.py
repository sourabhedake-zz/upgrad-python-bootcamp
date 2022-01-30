# Triple the list elements
# Description
# Given a list of integers, write a python code to triple all the values in the list.
# Note: Try using lambda and map functions to solve the problem.
# Input: A list of integers
# Output: A list of integers
# ----------------------------------------------------------------------
# Sample input: [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
# Output: [15, 21, 66, 291, 162, 186, 231, 69, 219, 183]
# ----------------------------------------------------------------------
# Sample input: [15, 71, 2, 9, 5, 6, 11, 3, 7, 6]
# Output: [45, 213, 6, 27, 15, 18, 33, 9, 21, 18]
# ----------------------------------------------------------------------
#take input here using ast sys
import ast
print(list(map(lambda x : x*3, inp)))