# Print Z
# Description
# Given a single positive integer 'n' greater than 2, create a NumPy array of size (n x n) will all zeros and ones such that the ones make a shape like 'Z'.
# Examples:
# Input 1:
# 3
# Output 1:
# [[1 1 1]
#  [0 1 0]
#  [1 1 1]]
# Input 2:
# 5
# Output 1:
# [[1 1 1 1 1]
#  [0 0 0 1 0]
#  [0 0 1 0 0]
#  [0 1 0 0 0]
#  [1 1 1 1 1]]
# Explanation: Notice that the 1s in the array make a shape like 'Z'.

# Read the input
n = int(input())

# Import the NumPy package
import numpy as np 

arr =np.zeros((n,n), dtype = int)

arr[0] = np.ones(1, dtype  = int)
arr[-1] = np.ones(1, dtype  = int)
for i in range(1, n):
    arr[i][n-i-1] = 1
print(arr)