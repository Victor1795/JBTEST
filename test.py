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
data1 = pd.read_csv('dummy_data.csv')        #semanal
#data2 = pd.read_csv('global_data.csv')       #current jira
data3 = pd.read_csv('new_global_data.csv')   #current jira with new epics

###### compare roleID vs Summary
df1 = pd.DataFrame(data1, columns=['Client', 'Role ID'])
#df2 = pd.DataFrame(data2, columns=['Summary', 'Issue id', 'Parent id', 'Issue type'])
df3 = pd.DataFrame(data3, columns=['Summary', 'Issue id'])

result = df1.join(df3, how = "outer") # Client(dummy feo), Role ID, Summary, Issue ID
#print(result)
## create new dataframe to compare 
df_primera = pd.DataFrame(columns= ['Summary','Issue key','Issue id','Parent id','Issue Type','Status'])


df_segunda = pd.DataFrame(data1, columns= ['Client','Project','Role Title','Role ID','IQN','POC','Resource Start Date','Role Created Date','Resource End Date'])


i = 0 # for role id (which ends up being both role id (custom) and summary
n = 0 # to bring the parent id to the subtask (which is the issue id of  the epic)

# iteration 
while i < result['Role ID'].count():
    x = result.loc[i,'Client']
    #c = result.loc[i,'Client']
    r = result.loc[i,'Role ID']
    y = 'Sub-task'
    z = 'OPEN' # status for now is on ????? maybe bc the dummy has on-hold, etc etc 
    

    boolean_finding = result['Summary'].str.contains(x).any()

    if(boolean_finding == True ): #True = create subTask  

####---------------------------------------------------------------------####
        p =[]
        while n < result['Summary'].count():
            #hor = 0
            #s = result.loc[n,'Client']
#            iid = result.loc[n,'Issue id']

            summary_finding = result['Summary'].str.contains(x).any().all()

                
            print(summary_finding)
            iid = result.loc[n,'Issue id']
            if(summary_finding == True):
                p.append(iid)

                print(p)

            n = n + 1

####---------------------------------------------------------------------####
#        boolean_finding = result['Summary'].str.contains(x).any()

        #p = result.loc[i, 'Issue id'] # p is supposed to find issue id within the epics only
        #print(p)
        v = [r,np.nan,np.nan,np.nan,y,z] #this is the final result where issue id of epic has been moved to parent id for the new subtask
        v1 = pd.Series(v, index = df_primera.columns)
        df_primera = df_primera.append(v1, ignore_index=True)
        
        df_final = df_primera.join(df_segunda, how = "outer")

        #s = [np.nan,x]
        #s1 = pd.Series(s, index = result.columns)
        #result = result.append(s1, ignore_index=True)
        df_final.to_csv("subtask_finaldata.csv", index=False)

    i = i + 1 # close while

print(df_primera)
print(df_final)
print(result)
