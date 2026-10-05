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



