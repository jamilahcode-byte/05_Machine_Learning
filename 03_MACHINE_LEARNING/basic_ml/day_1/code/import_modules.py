#import modules
import pandas as pd 
import numpy as np 
import sklearn.linear_model

#Load data 
oecd_bli = pd.read_csv("oecd_bli_2025.csv", thousands=",")
gdp_per_capita = pd.read_csv("gdb_per_capita.csv", thousands=",", delimiter='\t', encoding="latin1", na_values='n/a')


