# Compute the mean (Score) for each (Type) and return the result in descending order.
import numpy as np
import pandas as pd
from pandas import DataFrame

import requests , zipfile
from io import StringIO
import io

# Specify the url with data
url = 'https://github.com/Hernan4444/MyAnimeList-Database/archive/refs/heads/master.zip'

# Acquire data from the url
r = requests.get(url, stream=True)

# read and extract the zipfile
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall()

# Load and clean the data
anime_data = pd.read_csv('MyAnimeList-Database-master/data/anime.csv')
anime_data_extracted = anime_data[anime_data['Score'] != 'Unknown'].copy()
anime_data_extracted['Score'] = pd.to_numeric(anime_data_extracted['Score'])

def homework(anime_data_extracted):
    mean_grp = anime_data_extracted.groupby('Type')['Score'].mean()
    result = mean_grp.sort_values(ascending= False)
    return result

your_answer = homework(anime_data_extracted)
print(your_answer)


# NB:Our answer is a Series not a Data Frame.
# We got an error trying to using sort_values(by='Score') bcs it is only applicable in DataFrames not Series
# We remove the parameter
# groupby() splits the DataFrame into groups based on one or more
# columns. We can then perform an operation on each group,
# such as mean(), sum(), count(), min(), or max().


    
    



# print(anime_data_extracted['Score'])
# print(anime_data_extracted)