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
# Assuming the first row contains years and should be treated as headers
df = pd.read_csv('/Users/ethancratchley/desktop/appl_income_03.csv', header=None) 

# Prompt user for the row index of the data and type of plot
data_row = int(input("Enter the row index of the data to plot (e.g., 1 for Revenue): "))
plot_type = input("Enter the type of plot (line or bar): ").lower()

# Extract years and data based on user input and skip the first column
# Using ::-1 to reverse the order
years = df.iloc[0, 1:][::-1].values
data = df.iloc[data_row, 1:][::-1].values 

# Convert data to numeric, set errors='coerce' to replace non-numeric values with NaN
data = pd.to_numeric(data, errors='coerce')

# Handle NaN values if necessary - for example, we can replace them with zeros or interpolate
# Here, let’s replace NaN with zero - you can choose how to handle these as per your requirements
data = np.nan_to_num(data)

# Create a plot based on user input
if plot_type == 'line':
    plt.plot(years, data, marker='o', linestyle='-')
elif plot_type == 'bar':
    plt.bar(years, data)
else:
    print("Invalid plot type entered. Please enter either 'line' or 'bar'.")
    exit()

# Label the axes
plt.xlabel('Years')
plt.ylabel(df.iloc[data_row, 0])  # Automatically label y-axis based on the selected data row
plt.title(f'{df.iloc[data_row, 0]} Over Years')  # Automatically create title based on the selected data row

# Show the grid
plt.grid(True)

# Show the plot
plt.show()
















