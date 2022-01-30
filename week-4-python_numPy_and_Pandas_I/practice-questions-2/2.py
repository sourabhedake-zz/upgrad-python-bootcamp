# Sort by Column
# Description
# Given a 2D NumPy array, sort it by the 1st column. Print the final sorted array as a NumPy array only.
# Note: If two values in the 1st column are equal then the column in which the 2nd column value is lesser should come first. If the value in the second column is also the same then go to the third value and so on.
# Example:
# Input 1:
# [[9 3 2]
#  [4 0 1]
#  [5 8 6]]
# Output 2:
# [[4 0 1]
#  [5 8 6]
#  [9 3 2]]
# Input 2:
# [[9 3 2]
#  [4 0 1]
#  [9 8 6]]
# Output 2:
# [[4 0 1]
#  [9 3 2]
#  [9 8 6]]
# Explanation:
# Example 1: Notice that the values in the first column are sorted. Also notice that the whole row should be moved and not just the individual values in the first column. For example, the row with the smallest value, i.e. 4 was moved as a whole. 
# Example 2: Since this time the first row contains two 9s, the row in which the value in the second column is lesser came first.

# Reading the input list
import ast,sys
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)

# Import the NumPy package
import numpy as np

# Converting the list to a NumPy array
n_array = np.array(input_list)

for i in range(len(n_array[0])):
    n_array = n_array[n_array[:,-1-i].argsort()]
    
print(n_array)