# Removing Missing Values
# Description
# Consider the movie dataset again. Here are the first few rows of the same:﻿
# ﻿
# Now, while you imputed missing values in the last question, there are a few columns for which imputing the missing values won't be wise and it's better just to drop them. 
# There are two columns 'actor_1_facebook_likes' and 'actor_2_facebook_likes' which have quite a few missing values but since you have less data points, you don't want to drop many of them. For a hypothetical analysis that you're conducting, it will be okay if one of them has a missing value but you can't afford to have both missing values. So your aim here is to find the indices of the rows in which both of these columns have missing values simultaneously.
# Expected Output:
# - First print the indices of the rows where both these columns have missing values. The print statement has been provided in the stub. You just need to fill it. 
# - After you have printed the above indices, drop these particular rows and print the number of retained rows in the dataframe.
# A sample output would look like the following:
# [389, 1019, 1178, 3400, 4012]
# 4847
# Here, the list in the first line indicates a sample list which indicates the indices of the rows where both of the columns have missing values. And the second line represents the number of rows remaining in the dataframe after you have dropped the above rows.

import pandas as pd 

# Reading the dataframe
movies = pd.read_csv('https://media-doselect.s3.amazonaws.com/generic/ZY9xWvEzMB7NEoW08r52L8j2O/movie_data%20(1).csv')

# Find out the indices of the rows in which both these columns have missing values
print(list(movies[(movies['actor_1_facebook_likes'].isnull()) & (movies['actor_2_facebook_likes'].isnull())].index))

# Drop these particular rows
movies = movies[~((movies['actor_1_facebook_likes'].isnull()) & (movies['actor_2_facebook_likes'].isnull()))]

# Print the number of remaining rows
print(movies.shape[0])