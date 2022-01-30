# Series Sub-setting
# Description
# Given a Pandas series and a value 'n', write a program to create a subset of the series whose value is greater than 'n'.
# Input: The first line contains a 1D list that will be converted to a Pandas series, and the second line contains an integer 'n'.
# Output: Rows of the series whose value is less than n
# Sample Input 1: [0, 1,2,3,4,5,6,7,8,9,10]
# 6
# Sample Output 1: 
# 0  0
# 1  1
# 2  2
# 3  3
# 4  4
# 5  5
# Sample Input 2: [8, 1,14,0,7,5,6,7,13,9,10]
# 5
# Sample Output 2: 
# 1  1
# 3  0
import pandas as pd
import ast
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
inp_list=ast.literal_eval(input())
n=int(input())
s = pd.Series(inp_list)
news = s[s<n]
print(news)