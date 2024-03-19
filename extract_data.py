# Import all required packages
import os
import pandas as pd


# Copy the github URL of the raw csv file in the repo
source_url = 'https://raw.githubusercontent.com/YuehHanChen/Marketing_Analytics/main/marketing_data.csv'

# Extract the csv as a dataframes
customers_df = pd.read_csv(source_url)

# Check if destination directory exists
# Create the dir if it does not
dir_path = 'data'
if not os.path.exists(dir_path):
    os.makedirs(dir_path)

# Write the csv to a file in the data/ directory
customers_df.to_csv(dir_path + '/store_customers.csv')