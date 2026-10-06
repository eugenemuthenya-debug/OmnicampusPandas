import numpy as np
import pandas as pd
from pandas import Series,DataFrame
import numpy.random as random

# Libraries for downloading ZIP files nd files
# 1. Import libraries for downloading ZIP files and reading them we use :requests, zipfile,io

# requests->send and receive data from web
# zipfile->reads and write ZIP files
# io ->reads and writes files
import requests,zipfile
from io import StringIO
import io

# 1. We first use request.get()->to download the data from the url we specify
# 2. Use io.BytesIO() and zipfile.ZipFile() to extract the data as binary stream and store as a ZipFile object
# 3.Extract files from ZIP files using z.extractall()

# specify the url with data
url = 'https://github.com/Hernan4444/MyAnimeList-Database/archive/refs/heads/master.zip'

# Acquire data from url
r = requests.get(url, stream=True)

# read and extract the zipfile
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall()

# to view our data in hierarchical structure we use windows inbuilt feature called (tree / F) for linux we use (sudo apt-get install tree)

# LOADING AND CHECKING DATA
# We observe what kind of data anime.csv is.
# Reading data as a DataFrame.

# We read the data and treat it as pandas DataFrame object.
# To load a csv file as DataFrame object, we use pd.read_csv() and file name as an argument
anime_data = pd.read_csv('MyAnimeList-Database-master/data/anime.csv')
anime_list = pd.read_csv('MyAnimeList-Database-master/data/animelist.csv')
anime_synop = pd.read_csv('MyAnimeList-Database-master/data/anime_with_synopsis.csv')

# --------------------1.Checking data------------------
# We use .head() method to look at actual content.
# if nothing is specified in the parenthesis,the first five lines are displayed
# If you do specify then the specified number is displayed. eg: print(anime_data.head(10))
print(anime_data.head())

# ---------------------2.Checking nature of data----------
# To check the number of data we have and data type ,we use .info()
print(anime_data.info())

# we can also use describe to check various statistics about the quantitative data.
print(anime_data.describe())


# --------------DATAFRAME  BASICS-------------------------
# Transposition:(swap rows and columns)to transpose rows and columns as in the transposition of a matrix,refer to the (.T) attribute
print(anime_data.head().T)

# Data selection and Assignment
# How to select columns and rows
# 1.Extract only a specific column using [] or print(anime_data.Score)
print(anime_data['Score'])
print(anime_data.Score)

# Specify multiple columns as well,specify them in list form anime_data[['Name','Score']]
print(anime_data[['Score','Name']])

cols_to_use = ['MAL_ID','Name','Score','Genres','Type','Aired','Studios','Source','Members']
anime_data_extracted = anime_data[cols_to_use]
anime_data_extracted.head()

# Extracting only specific rows we use (:)
print(anime_data[0:3])

# same as to letters
# df['a':'c']


# Using df.loc[]
# Allows to retrieve a row or column by specifying the label(index or column name)
print(anime_data_extracted.loc[4])

# Specify row names(if multiple)
print(anime_data_extracted.loc[3:8])

# TO extract column ,you specify the column names after the comma.
anime_data_extracted.loc[:,['Name']]
# If multiple
anime_data_extracted.loc[:,['MAL_ID','Name']]
# combined row and column
anime_data_extracted[0:3,['MAL_ID','Name']]

# Using df.iloc[]
# retrieve a specific row or column but by specifying location(index number or column number)
# Specify first 4 rows and 1st and 3 column
print(anime_data_extracted.iloc[0:4,[0,2]])


# USing df.at and df.iat
# retrieve a specific element just like df.loc and df.iloc
print(anime_data.at[0,'Name'])

# Assigning and replacing values
# creating a new column can be done by using[] and name of new column.
# If you use a column name that already exist the data is overwritten
# df['Score'] = np.arrange(5)* 10
# to replace elements we can use the methods introduced
