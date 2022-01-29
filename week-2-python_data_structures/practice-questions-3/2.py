# List average
# Description
# Suppose you are working as a Marketing Lead in a company and you want to recruit new employees in your team (which already consists of 10 members) to carry out the company’s major project. You select the employees based on five parameters: A, B, C, D and E. The value of each parameter is represented on a scale of 1 to 10. The present average value of these parameters for your team is given to you in a list (in the same order). You recruit a person only if their scores do not reduce the average score of more than two parameters of your team. If they are recruited, print the output as ‘Selected’. If not, print the output as ‘Rejected’.
# --------------------------------------------------------------------------------------------------
# Input - Two lists, where the first list is the average scores of the team in the five parameters, and the second list is the scores of the new employee in all the five parameters. The parameter order is the same for both the lists, which is A, B, C, D and E.
# Output - String
# --------------------------------------------------------------------------------------------------
# Sample Input - [‘8’, ‘4’, ‘6’, ‘9’, ‘7’]
#   [‘1’, ‘1.1’, ‘1.2’, ‘1.2’, ‘2.3’]
# Sample Output - Rejected
# --------------------------------------------------------------------------------------------------
# Sample Input - [‘10’, ‘5’, ‘6’, ‘9’, ‘7’]
#   [‘10’, ‘ 9.8’, ‘7.2’, ‘1.66’, ‘4.3’]
# Sample Output - Selected
# --------------------------------------------------------------------------------------------------
# Sample Input - [‘8’, ‘5.66’, ‘6.5’, ‘10’, ‘10’]
#   [‘7’, ‘ 10’, ‘6’, ‘7’, ‘9’]
# Sample Output - Rejected
import ast

l1 = ast.literal_eval(input())
l2 = ast.literal_eval(input())

less = 0

for i in range(len(l1)):
    if l1[i] > l2[i]:
        less+=1

if (less > 2):
    print ("Rejected")
else:
    print ("Selected")
