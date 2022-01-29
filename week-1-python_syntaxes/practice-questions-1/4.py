# Valid triangle
# Description
# Write a program to accept three sides of a triangle as the input and print whether the triangle is valid or not.
# (A triangle is valid if the sum of any two sides is greater than the third side.)
# ----------------------------------------------------------------------
# Input:
# Three sides of a triangle separated by a space
# Output:
# Whether the given triangle is "Valid" or "Invalid"
# ----------------------------------------------------------------------
# Sample input:
# 3 4 5
# Sample output:
# Valid
# ----------------------------------------------------------------------
# Sample input:
# 1 4 5
# Sample output:
# Invalid

side = map(int, input().split())

side = sorted(side)
if (side[0] + side[1] > side[2]):
    print("Valid")
else:
    print("Invalid")
