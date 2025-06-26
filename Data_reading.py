import pandas as pd
from data_cleaning import *


# Reading the data from file
df = pd.read_csv('/Users/oblj-nkvarantan/PycharmProjects/F1 DATA/pit_stops_driver_race.csv') #reading data from file

print('Here is the data:' , df)

#print(df.head) #preview of first 5 rows

#df.info()
#df.describe()

df_remove_outs = pit_stop_outliers(df)
