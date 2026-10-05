# Preprocessing/cleaning data using Pandas(a python library)
# Pandas can:process data in form of DataFrames,join and cut data,create spreadsheets and handle time-series data,simple graphs
import pandas as pd
import numpy as np
import numpy.random as random
from pandas import Series, DataFrame


# Pandas data structure
# 1.Series:is a 1D object
# 2.DataFrame:is a 2D data sequence

# Series Object:It is like a numpy 1D array with labels
series = Series([1,2,3,4,5,8,13])
print(series)

# A series object comprises of Indices(left column) and Elements(right column)
# dtpye: represents data type = int64

# in NumPy:
a = np.array([1,2,3,4,5,8,13])
print(a)

# Indexing can be any number or character
series_i = Series([1,1,2,3,5,8,13],
                  index = ['a','b','c','d','e','f','g']
                  )
print(series_i)

# Elements and indices can be retrieved separately by specifying (values) and (index) attributes.
# Elements returned by the (values) attribute will be in NumPy array format.
# Index will show data type as well
print("Element:",series_i.values)
print("Index:",series_i.index)

# A DataFrame object is a 2D data column
# Below is a data structure with four columns:ID,CITY,BIRTH_year and Name.
# Key,value pair
# When displayed using print()-->data is in tabular form
data = {
    'ID':['100','101','102','103','104'],
    'City':['Tokyo','Osaka','Kyoto','Hokkaido','Tokyo'],
    'Birth_year':[1990,1989,1997,1992,1982],
    'Name':['Hiroshi','Akiko','Yuki','Satoru','Steve']
}
df = DataFrame(data)
print(df)
# The values on the left most column are = indices
# Any character can be used to specify the index of a DataFrame object
df_i = DataFrame(data,index=['a','b','c','d','e'])
print(df_i)
# We use the (values),(index),(columns) attributes to receive Elements,indices,columns
print('Element:',df_i.values)
print('Index:',df_i.index)
print('Column:',df_i.columns)

# When trying to display a huge DataFrame, it may be partially omitted. We can specify the maximum number of columns or rows to display below.
# pd-->pandas
# set_option-->tells pandas how to display the data.Specify what needs to be displayed using a string.
# specify max number of columns
pd.set_option('display.max_columns',50)

# specify max number of rows 
pd.set_option('display.max_rows',10)



