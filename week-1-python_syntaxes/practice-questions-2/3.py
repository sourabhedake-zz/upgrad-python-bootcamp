# Sum of digits
# Description
# Write a program to calculate the sum of the digits of a given number 
# ----------------------------------------------------------------------
# Input:
# An n digit number
# Output:
# Sum of the digits
# ----------------------------------------------------------------------
# Sample input:
# 983
# Sample output:
# 20
# ----------------------------------------------------------------------
# Sample input:
# 5241
# Sample output:
# 12
n=input()
summ = 0 
for i in n:
    summ += int(i)
print (summ)
