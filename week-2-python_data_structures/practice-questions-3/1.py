# Updating the dictionary keys
# Description
# You are provided with a dictionary containing the names of different football clubs as keys and the name of the main player of the corresponding team as values. When the main player of a team retires, one of their teammates steps up to fill in their role as the main player.
# You’re also provided with a list which contains the names of the football clubs for which the current main players are retiring and the names of the corresponding new main player. Your task is to update the values in the original dictionary with the names of the new main players.
# ------------------------------------------------------------------------------------------------------
# Input - The input consists of a dictionary with different football clubs' names and their main player. In the next line, you will be provided with a list of the new players who have taken up the main roles.
# Output - Dictionary
# ---------------------------------------------------------------------------------------------------
# Sample Input :
# {Barcelona:’Messi’ , ‘Real Madrid’: ‘Benzema’, ‘PSG’: ‘Neymar’ }
# [[‘Barcelona’, ‘Griezmann’], [‘PSG’, ‘Ramos’]]
# Sample Output: {Barcelona:‘Griezmann’, ‘Real Madrid’: ‘Benzema’, ‘PSG’: ‘Ramos’}
# ---------------------------------------------------------------------------------------------------
# Sample Input:
# {Liverpool:’A’, ‘Real Madrid’: ‘B’, ‘Chelsea’: ‘C’ }
# [[Liverpool, ‘R’]]
# Sample Output: {Liverpool:’R’, ‘Real Madrid’: ‘B’, ‘Chelsea’: ‘C’ }
# ---------------------------------------------------------------------------------------------------
# Sample Input :
#  {Atletico Madrid : ’D’ , ‘Juventus’: ‘B’, ‘Chelsea’: ‘C’ }
# [[‘Juventus’, ‘G’], [‘Chelsea’, ‘H’]]
# Sample Output: {Atletico Madrid : ’D’, ‘Juventus’: ‘G’, ‘Chelsea’: ‘H’ }
#Take input here
#we will take input using ast sys
import ast
#reading the input dictionary
input_dictionary = input()
convert_dictionary = ast.literal_eval(input_dictionary)

#reading the input list
input_list = input()
convert_list = ast.literal_eval(input_list)

#Write code here
for i in convert_list:
    convert_dictionary[i[0]] = i[1]
print (convert_dictionary)