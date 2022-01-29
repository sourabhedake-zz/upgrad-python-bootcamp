# String manipulation
# Description
# Write a program that takes a string as the input and does the following:
#     -Removes the numbers, special characters
#     -Converts uppercase letters to lowercase letters, and vice versa 
    
# ----------------------------------------------------------------------
# Input:
# A string 
# Output:
# A string with numbers, special characters removed, upper and lower cases swapped
# ----------------------------------------------------------------------
# Sample input:
# Programming1234
# Sample output:
# pROGRAMMING
# ----------------------------------------------------------------------
#  Sample input:
#  Programming is 100% fun
# Sample output:
# pROGRAMMINGISFUN

input_string=input()
s=""

for i in input_string:
    if (i.isalpha()):
        if i >= 'a':
            s += i.upper()
        else:
            s = i.lower()

print(s)
