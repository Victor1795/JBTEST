#!/usr/bin/env python3

import pandas as pd
import csv
import numpy as np




################################# NEW SUBTASK  / WHERE YOU NEED TO CHECK EPIC HAS BEEN CREATED BEFOREHAND AND THEN COMPARE ##################################
######### requeriments: 
#1 compare Client(Dummy) vs Summary(Jirav)
#2 If it exist use Role id(Dummy) as Summary(newCSV) and define Issue Type as Sub-task(newCSV)
#3 use Issue id(Jirav) to fill Parent id(newCSV) 
#4 copy rest of columns(newCSV)


######## read / bring over
data1 = pd.read_csv('dummy_data.csv')#,sep="\s+")
data2 = pd.read_csv('global_data.csv')#,sep="\s+")
data3 = pd.read_csv('')
###### compare roleID vs Summary
df1 = pd.DataFrame(data1, columns=['Client', 'Role ID'])
df2 = pd.DataFrame(data2, columns=['Summary', 'Issue id', 'Parent id', 'Issue type'])
result = df1.join(df2, how = "outer")

## create new dataframe to compare 
df = pd.DataFrame(columns= ['Summary', 'Role ID', 'Issue Type', 'Issue id', 'Parent id'])

i = 0 # for role id (which ends up being both role id (custom) and summary
n = 0 # to bring the parent id to the subtask (which is the issue id of  the epic)

# iteration 
while i < result['Role ID'].count():
    x = result.loc[i,'Role ID']
    y = 'Sub-task'
    
    #z = 'OPEN'
     
    boolean_finding = result['Role ID'].str.contains(x).any()

    if(boolean_finding == False ):
        p = result.loc[n, 'Parent id']
        if( 
        v = [x,x,y,np.nan,p]
        v1 = pd.Series(v, index = df.columns)
        #print(v)
        df = df.append(v1, ignore_index=True)
        #df.to_csv("epic_data.csv")
        s = [np.nan,x]
        s1 = pd.Series(s, index = result.columns)
        result = result.append(s1, ignore_index=True)
        df.to_csv("epic_data.csv", index=False)
# Find string in summary columns
        #print(df)
        #print(result)

# Returns true if the
        #print(boolean_finding)

#Outpu 
#True se hace automaticamente un subtask, false se crea constante issue type como epic 

    i = i + 1 # close while

print(df)
