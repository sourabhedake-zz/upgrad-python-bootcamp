# Data Analysis
# Description
# This time you've a fully cleaned movie dataset. The first few rows of the dataset are shown below:﻿
# ﻿
# You're a producer looking to make a blockbuster movie. There will primarily be three lead roles in your movie and you wish to cast the most popular actors for it. Now, since you don't want to take a risk, you will cast a trio which has already acted in together in a movie before. The metric that you've chosen to check the popularity is the Facebook likes of each of these actors.

# The dataframe has three columns to help you out for the same, viz. 'actor_1_facebook_likes', 'actor_2_facebook_likes', and 'actor_3_facebook_likes'. Your objective is to find the trio which has the most number of Facebook likes combined. But there is a small condition which is that none of the three actors' Facebook likes should be less than half of the other two. For example, the following is a valid combo:
# actor_1_facebook_likes: 70000
# actor_2_facebook_likes: 40000
# actor_3_facebook_likes: 50000

# But the below one is not:
# actor_1_facebook_likes: 70000
# actor_2_facebook_likes: 40000
# actor_3_facebook_likes: 30000

# since in this case, actor_3_facebook_likes is 30000, which is less than half of actor_1_facebook_likes.

# Expected Output: Find out the most popular trio and print them as a list sorted in alphabetical order. For example:
# ['Brad Pitt', 'Jake Gyllenhaal' 'Meryl Streep']
# Importing the pandas package
import pandas as pd

movies = pd.read_csv('https://media-doselect.s3.amazonaws.com/generic/pLLQowB8OYx0oBWdMbY4gp4wb/movies_final%20(2).csv', sep='\t')

group = movies.pivot_table(values = ['actor_1_facebook_likes', 'actor_2_facebook_likes', 'actor_3_facebook_likes'],
                           index = ['actor_1_name', 'actor_2_name', 'actor_3_name'], aggfunc='sum')
                           
# Create a new column 'Total likes' which will contain the sum of likes of all three actors 
group['Total likes'] = group['actor_1_facebook_likes'] + group['actor_2_facebook_likes'] + group['actor_3_facebook_likes']

# Sort the dataframe using the 'Total likes' column
group.sort_values(by=['Total likes'], inplace=True, ascending = False)

# Reset the index of the grouped dataframe so you can access the indices as columns easily
group.reset_index(inplace=True)

# Initialise the value of a variable 'j' to 0. This variable will be used to keep
# a track of the rows during the loop iteration
j = 0

# Run a loop through the length of the column 'Total likes'
for i in group['Total likes']:
# Sort the facebook likes of three actors and store them in a variable 'temp'    
    temp = sorted([group.loc[j,'actor_1_facebook_likes'], group.loc[j,'actor_2_facebook_likes'], group.loc[j,'actor_3_facebook_likes']])

# Check if the smallest value in temp is greater than half the value of the other two
# And also check if the middle value is greater than half the value of the max value
    if temp[0] >= temp[1]/2 and temp[0] >= temp[2]/2 and temp[1] >= temp[2]/2:
# If the above condition satisfies, print the correspoding actor names as a sorted list 
# and break the loop
        print(sorted([group.loc[j, 'actor_1_name'], group.loc[j, 'actor_2_name'], group.loc[j, 'actor_3_name']]))
        break
# Keep incrementing the value of j with every loop interation    
    j += 1 