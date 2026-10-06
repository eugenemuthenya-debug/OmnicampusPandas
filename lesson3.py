# ----------Extracting data with specific conditions------
# In a DataFrame object you can extract only data that specify a certain condition and combine multiple conditions as well
import numpy as np
import numpy.random as random
import pandas as pd
from pandas import Series,DataFrame

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

cols_to_use = ['MAL_ID','Name','Score','Genres','Type','Aired','Studios','Source','Members']
anime_data_extracted = anime_data[cols_to_use]
anime_data_extracted.head()

# Extracting only specific rows we use (:)
print(anime_data[0:3])

# Since our data set has some anime that does not have any scores, (Score=Unknown), we will exclude these rows using conditional filtering.

# The condition we specify, anime_data['Score'] != 'Unknown', returns a Series object whose dtype is bool

print(anime_data['Score'] != 'Unknown')

# Conditional Filtering
anime_data_extracted = anime_data_extracted[anime_data_extracted['Score'] != 'Unknown']
print(anime_data_extracted.head())

# To specify multiple conditions : enclose the expression with(). Use & for logical conjunction (AND) and | for logical disjunction(OR)

# Filters all anime produced by Nomad or Sunrise
print(anime_data_extracted[(anime_data_extracted['Studios'] =='Nomad') | (anime_data_extracted['Studios'] == 'Sunrise')].head())

# Use isin(list) as follows
# 'Studios' is either 'Sunrise' or 'Nomad'
print(anime_data_extracted[anime_data_extracted['Studios'].isin(['Sunrise','Nomad'])].head())

# 
print(anime_data_extracted[(anime_data_extracted['Source'] == 'Manga') | (anime_data_extracted['Members'] > 100000)])