# Merge dictionaries
# Description
# Write a python code to merge two dictionaries into a single dictionary.
# --------------------------------------------------------------------------------------------------
# Input: Two dictionaries, one in each line
# Output: A Dictionary
# --------------------------------------------------------------------------------------------------
# Sample Input :
# {'a': 10, 'b': 8}
# {'d': 6, 'c': 4}
# Sample Output : {'c': 4, 'a': 10, 'b': 8, 'd': 6}
# --------------------------------------------------------------------------------------------------
# Sample Input :
# {'a': 110, 'b': 88}
# {'d': 62, 'c': 44}
# Sample Output : {'a': 110, 'b': 88, 'd': 62, 'c': 44}
# --------------------------------------------------------------------------------------------------
import ast

d1 = ast.literal_eval(input())
d2 = ast.literal_eval(input())

for i in d2:
    d1[i] = d2[i]

print(d1)