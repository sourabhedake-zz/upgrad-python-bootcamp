# Length of list elements
# Description
# Given a list of strings, write a program to find the number of strings whose length is greater than or equal to K, where K is a positive integer.
# Input - List of strings and an integer
# ﻿Output - Integer
# --------------------------------------------------------------------------------
# Sample Input :
# [Mumbai, Hyderabad, Calicut, Chennai]
#   9
# Sample Output: 1
# -------------------------------------------------------------------------------
# Sample Input :
# [Datascience, Data Analyst, Programmer, Manager]
#   8
# Sample Output : 3
import ast
st = ast.literal_eval(input())
k = int(input())
cnt = 0
for i in st:
    if len(i) >= k:
        cnt +=1
print(cnt)