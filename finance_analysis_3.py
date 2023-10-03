import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Function to calculate and print descriptive statistics
def descriptive_statistics(df, index, metric_name):
    global mean, median, std_dev, min_value, min_year, max_value, max_year
    data = df.iloc[1:, index]
    data = pd.to_numeric(data, errors='coerce')

    mean = data.mean()
    median = data.median()
    std_dev = data.std()
    min_value = data.min()
    min_year = data.idxmin()
    max_value = data.max()
    max_year = data.idxmax()

    print(f'Mean {metric_name}: ${mean:.2f}')
    print(f'Median {metric_name}: ${median:.2f}')
    print(f'Standard Deviation of {metric_name}: ${std_dev:.2f}')
    print(f'Minimum {metric_name}: ${min_value:.2f} in the year {min_year}')
    print(f'Maximum {metric_name}: ${max_value:.2f} in the year {max_year}')
    print('-------------------------------------------------------------------------')


# Read the data and transpose the DataFrame
df = pd.read_csv('/Users/ethancratchley/desktop/appl_income_03.csv')
df_transposed = df.T

# Calculate descriptive statistics for different financial metrics
metrics = [("Revenue", 0), ("COGS", 3), ("Gross Income", 6), ("Net Income", 29)]

for metric_name, index in metrics:
    descriptive_statistics(df_transposed, index, metric_name)

# Print Stats for Diluted Shares Outstanding:
print('Mean Diluted Shares Outstanding: {:.2f}'.format(mean))
print('Median Diluted Shares Outstanding: {:.2f}'.format(median))
print('Standard Deviation of Diluted Shares Outstanding: {:.2f}'.format(std_dev))
print(f"Minimum Diluted Shares Outstanding: {min_value:.2f} in the year {min_year}")
print(f"Maximum Diluted Shares Outstanding: {max_value:.2f} in the year {max_year}")
print('-------------------------------------------------------------------------')


