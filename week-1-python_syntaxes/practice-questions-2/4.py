# Count the digits
# Description
# Write a program to accept a number from the user and count the zeros, odd digits and non-zero even digits from the entered number.
# ----------------------------------------------------------------------
# Input:
# A positive integer of n digits
# Output:
# Three integers representing the occurrences of zeros, odd digits and non-zero even digits from the entered number.
# ----------------------------------------------------------------------
# Sample input:
# 1030
# Sample output:
# Number of odd digits: 2
# Number of non-zero even digits: 0
# Number of zeros: 2
n=input()
z,e,o=0,0,0
for i in n:
    if (int(i)==0):
        z+=1
    elif int(i)%2 == 0:
        e+=1
    else:
        o+=1
    
print ("Number of odd digits:", o)
print ("Number of non-zero even digits:", e)
print ("Number of zeros:", z)
