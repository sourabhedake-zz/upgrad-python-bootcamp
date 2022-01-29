# Digit or Alphabet
# Description
# Write a program to display whether the input is a digit or a letter of the alphabet.
# ----------------------------------------------------------------------
# Input:
# A digit or a letter of the alphabet
# Output:
# Displays whether the given output is an integer or a letter of the alphabet
# ----------------------------------------------------------------------
# Sample input:
# 1
# Sample output:
# Integer
# ----------------------------------------------------------------------
# Sample input:
# b
# Sample output:
# Alphabet

inp=input()
if (inp[0] >= '0' and inp[0] <= '9'):
    print("Integer")
else:
    print("Alphabet")
