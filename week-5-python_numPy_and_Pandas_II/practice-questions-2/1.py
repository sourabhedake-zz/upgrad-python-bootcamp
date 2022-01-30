# Impute Missing Values
# Description
# You're given a movies dataframe which contains quite a few aspects of some movies from 1916-2016. Here are the first few rows of the dataframe.
# image.png 26.77 KB
# There are a lot of columns that aren't visible. But you might have noticed straight away that there are quite a few missing values in the data frame. Two columns for instance, 'aspect_ratio' and 'facenumber_in_poster' also have a few missing values(NaN). Now, replace the missing values with the 'median' value of the respective columns and print the null value count for both.
# Expected Output: First print the number of missing values in both of these columns, then output the median in both the columns and then impute the missing values with the respective medians and print the count of missing values again. Store all of these in a dictionary format like the following:
# {'aspect_ratio_mv': 431, 'facenumber_in_poster_mv': 97}
# {'aspect_ratio_median: 1.44, 'facenumber_in_poster': 2.0}
# {'aspect_ratio_final': 0, 'facenumber_in_poster_final': 0}
# The code for the same has been provided in the stub; you just need to complete these dictionaries.
# Note: You don't need to use any print statement. The print statements have already been written; you just need to complete the dictionaries provided in the stub.
import pandas as pd 

# Reading the movies dataframe
movies = pd.read_csv('https://media-doselect.s3.amazonaws.com/generic/1M2ZzY2M9PEBPJovgoaBgZdbM/movie_data.csv')

# Your aim is to complete the following three print statements after all the colons

# Get the null value counts in both the columns
aspect_ratio_mv = movies['aspect_ratio'].isnull().sum()
facenumber_in_poster_mv = movies['facenumber_in_poster'].isnull().sum()

# Complete the first dictionary
mv = {'aspect_ratio_mv': aspect_ratio_mv, 'facenumber_in_poster_mv': facenumber_in_poster_mv}

# Get the median of both the columns
aspect_ratio_median = movies['aspect_ratio'].median()
facenumber_in_poster_median = movies['facenumber_in_poster'].median()

# Complete the second dictionary
median = {'aspect_ratio_median': aspect_ratio_median, 'facenumber_in_poster_median': facenumber_in_poster_median}

movies.loc[pd.isnull(movies['aspect_ratio']), ['aspect_ratio']] = movies['aspect_ratio'].median()
movies.loc[pd.isnull(movies['facenumber_in_poster']), ['facenumber_in_poster']] = movies['facenumber_in_poster'].median()

# Get the final null value count of both the columns
aspect_ratio_final = movies['aspect_ratio'].isnull().sum()
facenumber_in_poster_final = movies['facenumber_in_poster'].isnull().sum()

# Complete the third dictionary
final = {'aspect_ratio_final': aspect_ratio_final, 'facenumber_in_poster_final': facenumber_in_poster_final}

# Printing the values in the three dictionaries. Please do not edit this part
print(sorted(mv.values()))
print(sorted(median.values()))
print(sorted(final.values()))