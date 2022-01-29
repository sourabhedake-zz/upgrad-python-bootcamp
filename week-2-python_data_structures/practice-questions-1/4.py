# Slicing a list
# Description
# Given a list of strings and an integer K, write a python code to print all the elements from the K th position till the end of the list.
# Note: Assume that K (a positive integer) will always be less than or equal to the length of the list
# Input - A list of strings in the first line and an integer in the second line of the input.
# Output - A list
# --------------------------------------------------------------------------------------------------------
# Sample Input :
# ['Mumbai', 'Delhi', 'Australia', 'Nigeria', 'USA', 'London', 'Canada']
# 2
# Sample Output : ['Delhi', 'Australia', 'Nigeria', 'USA', 'London', 'Canada']
# --------------------------------------------------------------------------------------------------------
# Sample Input :
# ['Chennai', 'Vizag', 'Austria', 'Germany', 'Japan']
# 3
# Sample Output : ['Austria', 'Germany', 'Japan']
#read the input using the ast sys
import ast
inp = ast.literal_eval(input())
k = int(input())
print(inp[k-1:])