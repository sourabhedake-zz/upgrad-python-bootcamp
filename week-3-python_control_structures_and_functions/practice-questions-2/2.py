# Intersection of lists
# Description
# In ‘ABC’ university, company ‘XYZ’ conducted three rounds of interviews to recruit students. Those students who passed all the rounds were selected. The company released the results for each round in a separate list. Your task is to write a Python code to display the list of the students who passed all the three rounds.
# Note: a. Name of the person can be given in uppercase or lowercase.
#  b. Print the names in lowercase in the output.
# Input: List
# List
# List
# Output: List
# ----------------------------------------------------------------------
# Sample input: ['Arkam', 'Bairstow', 'Cairy', 'Darpan'] 
#  ['ARKAM', 'Bairstow', 'Cairy', 'Darpan', 'Dhoni', 'Sachin']
#  ['arkam', 'bairstow', 'Cheteshwar', 'Dinesh']
        
# Sample output: ['arkam', 'bairstow']
# ----------------------------------------------------------------------
# Sample input: ['Pranay', 'Aditya', 'Deepesh', 'Sandesh']
# ['Pranoy', 'Surya', 'Cairy', 'Vignesh', 'ADITYA', 'SANDesh']
# ['Vardhan', 'Shailesh', 'aditya', 'sandesh']
        
# Sample output: ['aditya', 'sandesh']
# ----------------------------------------------------------------------
# Sample input: ['Siddharth', 'Gaurav', 'Prasad', 'Kuldeep', 'karna']
# ['siddharth', 'Gaurav', 'Prasad', 'Kuldeep', 'karna']
# ['Siddharth', 'gaurav', 'PRASAD', 'KuLDEEp', 'KARNA']
# Sample output: ['siddharth', 'gaurav', 'prasad', 'kuldeep', 'karna']
import ast
l1 = ast.literal_eval(input().lower())
l2 = ast.literal_eval(input().lower())
l3 = ast.literal_eval(input().lower())

ans = []
for x in l1:
    if x in l2 and x in l3:
        ans.append(x)
print(ans)