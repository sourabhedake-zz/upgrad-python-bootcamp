# Percentile
# Description
# Calculate the 60th percentile of the given NumPy array.
# Input: 1D array
# Output: Value of 60th percentile rounded off to two decimal places
# Sample Input 1: [11, 22, 33, 44 ,55 ,66, 77]
# Sample Output 1: 50.6
# Sample Input 2: [-1, 2, 0, 1, 3, 5, 3, 2, 1]
# Sample Output 2: 2.0
import numpy as np
import ast

#input has been taken for you
arr = np.array(ast.literal_eval(input()))
p = round(np.percentile(arr, 60), 2)
print(p)