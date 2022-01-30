# Series in Series
# Description
# Given two Pandas series, s1 and s2, write a program to print the elements of s1 that are not present in s2.
# Input: The first line has a 1D list containing elements of the first series, s1 and the second line has another 1D list containing elements of the second series, s2.
# Output: Rows of the series whose value.
# Sample Input 1: [1, 2, 3, 4, 5]
# [2, 4, 6, 8, 10]
# Sample Output 1: 
# 0  1
# 2  3
# 4  5
# Explanation:
# Series 1 and 2 have elements 2 and 4 in common. Hence, the elements that belong to s1 but not s2 are 1, 3 and 5. The output is in pandas series format containing the index of the elements also. 
# Sample Input 2: [8, 1,14,0,7,5,6,7,13,9,10]
# [0, 1,2,3,4,5,6,7,8,9,10]
# Sample Output 2: 
# 2  14
# 8  13
import pandas as pd
import ast
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
  
# Creating 2 pandas Series
ps1 = pd.Series(ast.literal_eval(input()))
ps2 = pd.Series(ast.literal_eval(input()))

res = ps1[~ps1.isin(ps2)]
print(res)