# Greater than 3
# Description
# Given an nxn array, print only the elements that are greater than three as a 1D array.
# Input: nxn array
# Output: 1D array containing elements that are greater than 3
# Sample Input 1: [[9,8,7],[6,5,4],[3,2,1]]
# Sample Output 1: [9 8 7 6 5 4]
# Sample Input 2: [[-1, 2, 0],[1,3,5],[3,2,1]]
# Sample Output 2: [5]
import numpy as np
import ast
#input has been taken for you
inp_list=ast.literal_eval(input())
arr=np.array(inp_list)

new_arr = arr[arr > 3]
print(new_arr)