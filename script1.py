#!/usr/bin/env python3
  
import pandas as pd
import csv

################################# Reading csv file & selecting important fields #####################################

data = pd.read_csv("TODOS.csv")

# selection
df = pd.DataFrame(data, columns= ['Client','Project','Role Title','Role ID','IQN','Status','POC','Resource Start Date','Role Created Date','Resource End Date'])

# create unique value field "Issue Type"
#df["Issue Type"] = 'Demand'

# save data 
df.to_csv("global_data.csv") #, index=False)
