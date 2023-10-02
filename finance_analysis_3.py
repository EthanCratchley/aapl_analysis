import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/ethancratchley/desktop/appl_income_03.csv')

# Transpose the DataFrame to swap rows with columns
df_transposed = df.T

# To Do: Calculate Stats for: Gross Income, Net Income, Diluted Shares Outstanding, EBIT 

# Descriptive Statistics:

descriptive_stats = []

# Calculate Stats for Revenue:
# Select Row:
sales_data = df_transposed.iloc[1:, 0]

# Convert the sales data to numeric, errors='coerce' will replace non-numeric values with NaN
sales_data = pd.to_numeric(sales_data, errors='coerce')

# Calculate the Stats
mean_sales = sales_data.mean()
median_sales = sales_data.median()
std_sales = sales_data.std()

# Get Min and Max with the corresponding year
min_sales = sales_data.min()
min_sales_year = sales_data.idxmin()
max_sales = sales_data.max()
max_sales_year = sales_data.idxmax()

# Append to Stats List
descriptive_stats.append(mean_sales)
descriptive_stats.append(median_sales)
descriptive_stats.append(std_sales)
descriptive_stats.append(min_sales)
descriptive_stats.append(min_sales_year)
descriptive_stats.append(max_sales)
descriptive_stats.append(max_sales_year)

# Print Stats:
print('Mean Revenue: ${:.2f}'.format(mean_sales))
print('Median Revenue: ${:.2f}'.format(median_sales))
print('Standard Deviation of Revenue: ${:.2f}'.format(std_sales))
print(f"Minimum Revenue: ${min_sales:.2f} in the year {min_sales_year}")
print(f"Maximum Revenue: ${max_sales:.2f} in the year {max_sales_year}")

# Calculate Stats for COGS

# Select Row:
cogs_data = df_transposed.iloc[1:, 3]

# Convert the COGS data to numeric, errors='coerce' will replace non-numeric values with NaN
cogs_data = pd.to_numeric(cogs_data, errors='coerce')

# Calculate the Stats
mean_cogs = cogs_data.mean()
median_cogs = cogs_data.median()
std_cogs = cogs_data.std()

# Get Min and Max with the corresponding year
min_cogs = cogs_data.min()
min_cogs_year = cogs_data.idxmin()
max_cogs = cogs_data.max()
max_cogs_year = cogs_data.idxmax()

# Append to Stats List:
descriptive_stats.append(mean_cogs)
descriptive_stats.append(median_cogs)
descriptive_stats.append(std_cogs)
descriptive_stats.append(min_cogs)
descriptive_stats.append(min_cogs_year)
descriptive_stats.append(max_cogs)
descriptive_stats.append(max_cogs_year)

# Print Stats:
print('Mean COGS: ${:.2f}'.format(mean_cogs))
print('Median COGS: ${:.2f}'.format(median_cogs))
print('Standard Deviation of COGS: ${:.2f}'.format(std_cogs))
print(f"Minimum COGS: ${min_cogs:.2f} in the year {min_cogs_year}")
print(f"Maximum COGS: ${max_cogs:.2f} in the year {max_cogs_year}")

