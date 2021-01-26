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
data3 = pd.read_csv('actual_epics.csv')

###### compare roleID vs Summary
df1 = pd.DataFrame(data1, columns=['Client', 'Role ID'])
df2 = pd.DataFrame(data2, columns=['Summary', 'Issue id', 'Parent id', 'Issue type'])
df3 = pd.DataFrame(data3, columns=['Summary', 'Issue id'])

result = df1.join(df2, how = "outer")

## create new dataframe to compare 
df = pd.DataFrame(columns= ['Summary', 'Role ID', 'Issue Type', 'Issue id', 'Parent id'])

i = 0 # for role id (which ends up being both role id (custom) and summary
n = 0 # to bring the parent id to the subtask (which is the issue id of  the epic)

# iteration 
while i < result['Role ID'].count():
    x = result.loc[i,'Role ID']
    y = 'Sub-task'
    
    #z = 'OPEN' status for now is on ????? maybe bc the dummy has on-hold, etc etc 
     
    boolean_finding = result['Role ID'].str.contains(x).any()

    if(boolean_finding == False ): #first if refers to 
        p = result.loc[n, 'Parent id'] # p is supposed to find issue id within the epics only
        if( 
        v = [x,x,y,np.nan,p] #this is the final result where issue id of epic has been moved to parent id for the new subtask
        v1 = pd.Series(v, index = df.columns)
        
        df = df.append(v1, ignore_index=True)
        
        s = [np.nan,x]
        s1 = pd.Series(s, index = result.columns)
        result = result.append(s1, ignore_index=True)
        df.to_csv("epic_data.csv", index=False)




    i = i + 1 # close while

print(df)
