#!/usr/bin/env python3

import pandas as pd
import csv

################################# Reading csv file & selecting important fields #####################################
data = pd.read_csv("global_data.csv")

print(data)
