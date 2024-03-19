# Import all required packages
import pandas as pd

# Read and create a dataframe for store customers data
file_path = 'data/store_customers.csv'
customers_df = pd.read_csv(file_path)

# Displays all columns of the table, no truncation
pd.set_option('display.max_columns', None)

# View basic statistics about the dataframe
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

# Assessment report from observing the above statistics
print('Issues in the dataframe :')
print('* Space before and after the Income column name')
print('* Dollar signs, spaces, commas in the values of Income column')
print('* Income column has string data type where 24 are null')
print('* Dt_Customer\'s data type is string')