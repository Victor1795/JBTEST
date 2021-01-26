#!/usr/bin/env python3

import pandas as pd
import csv
import numpy as np
from itertools import permutations


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
print(resultado) 



#summary = result.loc[0,'Client']
        #df.loc(i,'Summary').append("x")
        #print(df)


#v = pd.DataFrame(data= [summary])
#df.append(summary)
#print(df)
#print(v)


#df = pd.DataFrame(columns={'Summary', 'Issue Type', 'Role Id'},  index=[x])


i = 0
#print(i)
# iteration starts 
# Iterating using while loop
while i < x['Client'].count():
    #x = result.loc[i,'Client']
    #df["Summary"] = x
    #df["Issue Type"] = 'Epic'
    #df["Status"] = 'OPEN'
    #print(df)
    #print(i)
    #print(x
    b = x.loc[i,'Client']
    boolean_finding = x['Summary'].str.contains(b).any()

    if(boolean_finding == False):
    # x = result.loc[i,'Client']
        #df["Summary"] = b
        #df["Issue Type"] = 'Epic'
        #df["Status"] = 'OPEN'
        print(x) 

    #summary = result.loc[i,'Client']    
        #df.loc(i,'Summary').append("x")
        #print(df)
        #v = pd.DataFrame([summary])
        #df.append(v)
        #print(df)
        #df.loc(i, 'Issue Type') = 'Epic'
    #df.loc(i, 'Status') = 'OPEN'


        # issue type = epic
    # solo necesita summary & client, que es el mismo (cliente)
 
    #else 
    # issue type = sub-task, y que copie su role ID a Summary

# Returns true if the
#print(boolean_finding)

#Outpu 
#True se hace automaticamente un subtask, false se crea constante issue type como epic 

i = i + 1 # close while
#print(df)
