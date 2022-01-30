# Even numbers in a list
# Description
# Given a list of integers, write a python code to find all the even numbers present in the list.
# Note: Try using lambda and filter functions to solve the problem.
# Input: A list of integers
# Output: A list of integers
# ----------------------------------------------------------------------
# Sample input: [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 
# Sample output: [22, 54, 62]
# ----------------------------------------------------------------------
# Sample input: [500, 789, 2112, 9097, 5894, 9062, 8977, 1223, 773, 600]
# Sample output: [500, 2112, 5894, 9062, 600]
# ----------------------------------------------------------------------
#take input here using ast sys
import ast
inp = ast.literal_eval(input())

print(list(filter(lambda x : x%2==0, inp)))