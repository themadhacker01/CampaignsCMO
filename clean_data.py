# Import all the required packages
import pandas as pd

# Extract the csv values into a dataframe
file_path = 'data/store_customers.csv'
customer_data = pd.read_csv(file_path)

# Display all table columns, no truncation
pd.set_option('display.max_columns', None)

# Create a copy of the dataframe
customer_data_copy = customer_data.copy()


# Issue 1 : Remove the space in front of Income column
customer_data_copy.rename(columns = {' Income ': 'Income'}, inplace = True)
print(customer_data_copy.columns)


# Issue 2 : Dollar signs, spaces, commas in the values of Income column
customer_data_copy.Income = customer_data_copy.Income.str.strip('$')
customer_data_copy.Income = customer_data_copy.Income.str.replace('.', '')
customer_data_copy.Income = customer_data_copy.Income.str.replace(',', '')
customer_data_copy.Income = customer_data_copy.Income.str.replace('00', '')
print(customer_data_copy.Income.sample(5))


# Issue 3 : Income column has 24 missing values
# Issue 4 : Income's type is string

# Seperate dataframe into valid vs null values
null_income = customer_data_copy[customer_data_copy.Income.isnull() == True]
valid_income = customer_data_copy[customer_data_copy.Income.isnull() == False]

# Replace null values with 0, convert to int
null_income.Income = '0'
null_income.Income = null_income.Income.astype(int)
print(null_income.info())

# Convert rows with valid incomes to to type int
valid_income.Income = valid_income.Income.astype(int)

# Reset the dataframe value by combining the cleaned Income column
customer_data_copy = null_income._append(valid_income)
print(customer_data_copy.info())


# Issue 5 : Dt_Customer's data type is string
customer_data_copy.Dt_Customer = pd.to_datetime(customer_data_copy.Dt_Customer, format = '%m/%d/%y')
print(type(customer_data_copy.Dt_Customer.iloc[1]))