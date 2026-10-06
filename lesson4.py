# Determination of nan(null)

import numpy as np
import numpy.random as random
import pandas as pd
from pandas import Series,DataFrame

# Data may be missing and the corresponding data may not exist, and if calculated correct values won't be obtained when average and other calculations are done.
# Data such as missing values are sorted with a special value called (nan)

# we can use isnull() to check if element is nan
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

cols_to_use = ['MAL_ID','Name','Score','Genres','Type','Aired','Studios','Source','Members']
anime_data_extracted = anime_data[cols_to_use]
anime_data_extracted.head()

# Extracting only specific rows we use (:)
print(anime_data[0:3])
print(anime_data_extracted.isnull())

# to find the total number of null values we use .sum()
print(anime_data_extracted.isnull().sum())

# we check other data sets
print(anime_list.isnull())
# sum of all null values
print(anime_list.isnull().sum())

print(anime_synop.isnull().sum())

# --------------Sorting Values--------------------------
# Sorting can be done idex wise or element wise
# By index .sort_index()
print(anime_data_extracted.sort_index())

# By values .sort_values()
# The default is ascending order but you can specify ascending or descending order
print(anime_data_extracted.sort_values(by = 'Score',ascending=False))
