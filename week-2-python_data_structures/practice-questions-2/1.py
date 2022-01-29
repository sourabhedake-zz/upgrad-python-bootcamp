# Substring with maximum uppercase characters
# Description
# Given a string, write a Python program to find the largest substring of uppercase characters and print the length of that substring. Check the sample inputs and outputs for a better understanding.
# ---------------------------------------------------------------------------------------------------
# Input - String
# Output - String
# ---------------------------------------------------------------------------------------------------
# Sample Input - I lovE PRogrAMMING
# Sample Output - 6
# Explanation - AMMING is the largest substring with all characters in uppercase continuously 
# -----------------------------------------------------------------------------------------------------
# Sample Input - MuMbaI is in MAHArashTRA
# Sample Output - 4
# Explanation - MAHA is the largest substring with all characters in uppercase continuously.
# ---------------------------------------------------------------------------------------------------
# Sample Input - India WOn the WOrLD CUP
# Sample Output - 3
# Explanation - CUP is the largest substring with all characters in uppercase continuously.
#Take input here
test_str = input()

max_u = 0
u = 0
for i in test_str:
    if i.isupper():
        u+=1
        if max_u < u:
            max_u = u
    else:
        u= 0
print (max_u)