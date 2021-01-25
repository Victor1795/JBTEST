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



df_data = open("df_data.csv", "w")

# to show the fields that are important to you
df = pd.DataFrame(data, columns= ['Client','Project','Role Title','Role ID','IQN','Status','POC','Resource Start Date','Role Created Date','Resource End Date'])

#print (df, file=df_data)
df_data.close()
df["Issue Type"] = 'Demand'
df.to_csv("df_data.csv", index=False)




i = 0
#print(i)
# iteration starts 
# Iterating using while loop
while i < result['Client'].count():
    x = result.loc[i,'Client']
    print(i)
    print(x)
    boolean_finding = result['Summary'].str.contains(x).any()

    if(boolean_finding == False ):
    
# Find string in summary column
    else 


# Returns true if the
print(boolean_finding)

#Outpu 
#True se hace automaticamente un subtask, false se crea constante issue type como epic 



    


    i = i + 1 # close while
