# Multiplication Table
# Description
# Write a program to display the multiplication table of a given number.
# ----------------------------------------------------------------------
# Input:
# A positive integer
# Output:
# Multiplication table
# ----------------------------------------------------------------------
# Sample input:
# 5
# Sample output:
# 5 * 1 = 5
# 5 * 2 = 10
# 5 * 3 = 15
# 5 * 4 = 20
# 5 * 5 = 25
# 5 * 6 = 30
# 5 * 7 = 35
# 5 * 8 = 40
# 5 * 9 = 45
# 5 * 10 = 50
n=int(input())

for i in range(1, 11):
    print(n, "*", i, "=", n*i)
