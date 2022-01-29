# No Vowels
# Description
# Write a program to accept a string from the user, delete all vowels from the string and display the result. 
# ----------------------------------------------------------------------
# Input:
# A string
# Output:
# A string with vowels removed
# ----------------------------------------------------------------------
# Sample input:
# Upgrad
# Sample output:
# pgrd
# ----------------------------------------------------------------------
# Sample input:
# Python Programming
# Sample output:
# Pythn Prgrmmng


s=input()
f=""
v="aeiouAEIOU"

for i in s:
    if i not in v:
        f+=i

print(f)
