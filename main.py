# Import all required packages
import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sb

# Read and create a dataframe for store customers data
file_path = 'data/store_customers.csv'
customers_df = pd.read_csv(file_path)

# Displays all columns of the table, no truncation
pd.set_option('display.max_columns', None)

# Assess the data and view basic information about it
print()
print('First five columns of the database :\n', customers_df.head())
print()
print(customers_df.shape[0], 'rows x ', customers_df.shape[1], ' columns')
print()
print(customers_df[customers_df.duplicated()].shape[0], ' duplicate rows')
print()
print('Basic statistics about the database :\n', customers_df.describe())
print()
print('Information about columns :\n', customers_df.info())