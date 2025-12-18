# Walmart Sales Data Visualization Report

## Dataset Overview

The Walmart sales dataset contains information about weekly sales across multiple stores. The dataset includes the following columns:
- **Store**: Store identifier
- **Date**: Week date
- **Weekly_Sales**: Total sales for the week
- **Holiday_Flag**: Indicates if the week is a holiday week (1) or not (0)
- **Temperature**: Average temperature during the week
- **Fuel_Price**: Fuel price during the week
- **CPI**: Consumer Price Index
- **Unemployment**: Unemployment rate
- **District**: District identifier

## Visualization Tools and Techniques

Based on the dataset structure, here are several visualization tools in Python that could be applied:

### 1. Matplotlib
Matplotlib is the fundamental plotting library in Python. It can be used to create:
- Time series plots showing weekly sales trends over time
- Scatter plots to examine relationships between variables
- Bar charts comparing sales across different stores or districts

### 2. Seaborn
Seaborn is built on top of matplotlib and provides a higher-level interface for statistical graphics:
- Heatmaps to show correlations between numerical variables
- Box plots to visualize the distribution of sales data
- Regression plots to examine relationships with confidence intervals

### 3. Pandas Built-in Plotting
Pandas provides convenient plotting functions directly on DataFrame objects:
- Histograms to show the distribution of sales, temperature, fuel prices, etc.
- Line plots for time series visualization
- Scatter matrix plots to quickly examine relationships between multiple variables

### 4. Plotly
Plotly creates interactive visualizations that can be embedded in web applications:
- Interactive time series charts with hover information
- 3D scatter plots to examine relationships between three variables
- Dashboards combining multiple visualizations

## Sample Implementation Code

Below is an example of how to implement some of these visualizations:

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('/Users/simonwang/Documents/Usage/MathAI/MscMinicourse/Data/Walmart2.csv')

# Time series plot of weekly sales
plt.figure(figsize=(12, 6))
df.groupby('Date')['Weekly_Sales'].sum().plot()
plt.title('Total Weekly Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Correlation heatmap
plt.figure(figsize=(10, 8))
correlation_matrix = df[['Weekly_Sales', 'Temperature', 'Fuel_Price', 'CPI', 'Unemployment']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Matrix of Numerical Variables')
plt.tight_layout()
plt.show()

# Box plot comparing sales by holiday flag
plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x='Holiday_Flag', y='Weekly_Sales')
plt.title('Sales Distribution: Holiday vs Non-Holiday Weeks')
plt.xlabel('Holiday Flag (0=Non-Holiday, 1=Holiday)')
plt.ylabel('Weekly Sales')
plt.tight_layout()
plt.show()
```

## Explanation of Visualization Choices

1. **Time Series Plot**: This visualization helps identify seasonal patterns, trends, and anomalies in sales data over time.

2. **Correlation Heatmap**: This helps understand relationships between variables. For example, we might find that fuel prices negatively correlate with sales, suggesting that when gas prices are high, people spend less at Walmart.

3. **Box Plot by Holiday Flag**: This compares the distribution of sales during holiday weeks versus regular weeks, helping to quantify the impact of holidays on sales performance.

These visualizations provide insights into sales patterns, external factors affecting sales, and help identify opportunities for business improvement.