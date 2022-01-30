# Rename Columns
# Description
# You have been given a dataset called 'heart'. Here are its first few rows:﻿
# ﻿
# As you can see, the column names are all lowercase. Your task is to capitalize the first character of every column present in it such that your dataframe looks like the following:﻿
# ﻿
# You just need to write the code for capitalizing; you need not print anything as the print statement has already been provided in the stub.
import pandas as pd
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
# Reading the dataframe
df = pd.read_csv('https://media-doselect.s3.amazonaws.com/generic/XWvQjYY4LZWdxLvPWOj2pPwn/heart.csv')
df.columns = df.columns.str.capitalize()

# Printing the final columns. Do not edit this part.
print(df.columns)