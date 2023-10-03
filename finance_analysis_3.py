import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Function to calculate and print descriptive statistics
def descriptive_statistics(df, index, metric_name):
    data = df.iloc[1:, index]
    data = pd.to_numeric(data, errors='coerce')

    stats = {
        "mean": data.mean(),
        "median": data.median(),
        "std_dev": data.std(),
        "min_value": data.min(),
        "min_year": data.idxmin(),
        "max_value": data.max(),
        "max_year": data.idxmax()
    }

    if "Shares" in metric_name:
        print(f'Mean {metric_name}: {stats["mean"]:.2f}')
        print(f'Median {metric_name}: {stats["median"]:.2f}')
        print(f'Standard Deviation of {metric_name}: {stats["std_dev"]:.2f}')
        print(f'Minimum {metric_name}: {stats["min_value"]:.2f} in the year {stats["min_year"]}')
        print(f'Maximum {metric_name}: {stats["max_value"]:.2f} in the year {stats["max_year"]}')
        print('-------------------------------------------------------------------------')
    else:
        print(f'Mean {metric_name}: ${stats["mean"]:.2f}')
        print(f'Median {metric_name}: ${stats["median"]:.2f}')
        print(f'Standard Deviation of {metric_name}: ${stats["std_dev"]:.2f}')
        print(f'Minimum {metric_name}: ${stats["min_value"]:.2f} in the year {stats["min_year"]}')
        print(f'Maximum {metric_name}: ${stats["max_value"]:.2f} in the year {stats["max_year"]}')
        print('-------------------------------------------------------------------------')

    return stats


# Read the data and transpose the DataFrame
df = pd.read_csv('/Users/ethancratchley/desktop/appl_income_03.csv')
df_transposed = df.T

# Calculate descriptive statistics for different financial metrics
metrics = [("Revenue", 0), ("COGS", 3), ("Gross Income", 6), ("Net Income", 29), ("Diluted Shares Outstanding", 39)]

for metric_name, index in metrics:
    descriptive_statistics(df_transposed, index, metric_name)

# Graphing and Data Visualization:

# To Do: Revenue, Sales Growth, COGS Growth, Gross Income, Net Income, Net Income Growth, EPS   

# Function to plot line chart
def line_chart(df, index, data_name):
    data = df.iloc[1:, index]
    years = df.iloc[0, 1:]  # Corrected this line
    data = pd.to_numeric(data, errors='coerce')

    plt.figure(figsize=(10, 6))
    plt.plot(years, data)  
    plt.xlabel('Year')
    plt.ylabel(data_name)
    plt.title(f'{data_name} Over the Years')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

# Function to plot bar chart
def bar_chart(df, index, data_name):
    data = df.iloc[1:, index]
    years = df.iloc[0, 1:]  # Corrected this line
    data = pd.to_numeric(data, errors='coerce')

    plt.figure(figsize=(10, 6))
    plt.bar(years, data)
    plt.xlabel('Year')
    plt.ylabel(data_name)
    plt.title(f'{data_name} Over the Years')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

# Testing the plotting functions
df = pd.read_csv('/Users/ethancratchley/desktop/appl_income_03.csv')
df_transposed = df.T

metrics = [("Revenue", 0), ("COGS", 3)]

for metric_name, index in metrics:
    line_chart(df_transposed, index, metric_name)
    bar_chart(df_transposed, index, metric_name)
