#!/usr/bin/env python3

import pandas as pd
import csv
import numpy as np
#from pandas.testing import assert_frame_equal



################################# NEW EPIC / WHERE YOU NEED TO COMPARE FIRST TO SEE IF IT EXISTS  #####################################
######### requeriments: 
##### 1 compare Client(Dummy) vs Summary(Jirav) // COMPARA
####  2 If not found (false) define Issue Type as Epic(newCSV) // IF
####  3 Use Client(Dummy) as Summary(newCSV) // COMPARA 
####  4 set Status OPEN(newCSV) // #3 es condicional 


# new csv is newcsv

######## read / bring over
# dummy_data.csv
# global_data.csv
data1 = pd.read_csv('dummy_data.csv')#,sep="\s+")
data2 = pd.read_csv('global_data.csv')#,sep="\s+")

###### compare roleID vs Summary
df1 = pd.DataFrame(data1, columns=['Client'])


df2 = pd.DataFrame(data2, columns=['Summary'])


result = df1.join(df2, how = "outer")

## create new column to check. true= theyre already a subtask, false means we need to add them as new ones and use the ID as summary
print(result) # nuevo dataframe



x = result.loc[0,'Client']
print(x)

# Find string in summary column
boolean_finding = result['Summary'].str.contains(result.loc[0,'Client']).any()

# Returns true if the
print(boolean_finding)

#Output
# True se hace automaticamente un subtask, false se crea constante issue type como epic 

# condicional if(boolean_finding):
    

