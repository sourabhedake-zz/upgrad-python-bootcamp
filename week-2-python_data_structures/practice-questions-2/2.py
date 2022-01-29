# Sorting list of tuples
# Description
# A class of students attempt an exam in two parts: ‘Aptitude’ and ‘Physics'. The marks of all the students are stored as a list of tuples, and each student’s marks (in Aptitude and Physics) are stored in each tuple. Your task is to write a Python program to sort the list of tuples in decreasing order of the Physics scores of the students.
# Note - Marks of both the subjects are ranged between 1-100, and no two students have scored the same marks in Physics.
# ---------------------------------------------------------------------------------------------------
# Input - List of tuples
# Output - List of tuples
# ---------------------------------------------------------------------------------------------------
# Sample Input - [(45,77), (88,87), (67,98), (33,31)]
# In (45,77), which is the first element in the list, 45 and 77 are the scores of a student in aptitude and physics respectively.
# Sample Output - [ (67,98), (88,87), (45,77),(33,31)]
# ---------------------------------------------------------------------------------------------------
# Sample Input - [(45,23), (45,88), (45,98), (45,44)]
# Sample Output - [ (45,98), (45,88), (45,44),(45,23)]
# ---------------------------------------------------------------------------------------------------
# Sample Input - [(55,77), (34,90), (67,100), (90,0)]
# Sample Output - [ (67,100), (34,90), (55,77),(90,0)]
#Take input 
import ast

inp = ast.literal_eval(input())

def fun(q1,q2):
    return q1[1] > q2[1]
    
inp.sort(key=lambda x : x[1],  reverse=True)
print(inp)