#!/usr/bin/env python3
  
import pandas as pd
import csv

################################# Reading csv file & selecting important fields #####################################

data = pd.read_csv("TODOS.csv")

# selection
df = pd.DataFrame(data, columns= ['Summary','Issue key','Issue id','Parent id','Issue Type','Status','Custom field (POC JBT)','Custom field (Role Title)','Custom field (IQN)','Custom field (Client JBT)','Custom field (Project JBT)','Custom field (Role Title)','Custom field (Role Id)','Custom field (Resource Start Date)','Custom field (Role Created)','Custom field (Resource End Date)'])

# create unique value field "Issue Type"
#df["Issue Type"] = 'Demand'

# save data 
df.to_csv("global_data.csv") #, index=False)
