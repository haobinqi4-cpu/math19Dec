#!/usr/bin/env python3
"""
Generate visualizations for the Walmart dataset and save as HTML with descriptions.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime
import os
import base64
from io import BytesIO

# Set style for better-looking plots
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

def save_plot_to_base64():
    """Save current plot to base64 string for embedding in HTML"""
    buffer = BytesIO()
    plt.savefig(buffer, format='png', dpi=300, bbox_inches='tight')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')
    plt.close()
    return graphic

def create_html_report(plots_data):
    """Create HTML report with embedded plots and descriptions"""
    html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Walmart Sales Data Visualization Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; }}
        h1, h2 {{ color: #2c3e50; }}
        .plot-container {{ margin: 30px 0; }}
        .plot-image {{ max-width: 100%; height: auto; }}
        .description {{ background-color: #f8f9fa; padding: 15px; border-left: 4px solid #007bff; margin: 15px 0; }}
        .footer {{ margin-top: 50px; padding-top: 20px; border-top: 1px solid #eee; color: #6c757d; }}
    </style>
</head>
<body>
    <h1>Walmart Sales Data Visualization Report</h1>
    
    <div class="description">
        <p>This report presents visual analysis of Walmart sales data across multiple stores over time. 
        The dataset includes information on weekly sales, holidays, temperature, fuel prices, economic indicators, 
        and other factors that may influence retail performance.</p>
    </div>
    
    {}
    
    <div class="footer">
        <p>Report generated on {}</p>
    </div>
</body>
</html>
    """
    
    plot_sections = ""
    for plot_data in plots_data:
        section = f"""
    <div class="plot-container">
        <h2>{plot_data['title']}</h2>
        <div class="description">
            <p>{plot_data['description']}</p>
        </div>
        <img src="data:image/png;base64,{plot_data['image']}" alt="{plot_data['title']}" class="plot-image">
    </div>
        """
        plot_sections += section
    
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return html_template.format(plot_sections, current_date)

def load_and_prepare_data(filepath):
    """Load and prepare the Walmart dataset"""
    df = pd.read_csv(filepath)
    
    # Convert date column to datetime (day-first format)
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
    
    # Sort by date for time series analysis
    df = df.sort_values('Date')
    
    return df

def plot_sales_over_time(df):
    """Create time series plot of total weekly sales"""
    # Aggregate sales by date
    daily_sales = df.groupby('Date')['Weekly_Sales'].sum()
    
    plt.figure(figsize=(12, 6))
    plt.plot(daily_sales.index, daily_sales.values, linewidth=2, color='#2E86AB')
    plt.title('Total Weekly Sales Over Time', fontsize=16, pad=20)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Total Sales ($)', fontsize=12)
    plt.grid(True, alpha=0.3)
    
    return save_plot_to_base64()

def plot_sales_by_store(df):
    """Create bar chart of average sales by store"""
    store_avg = df.groupby('Store')['Weekly_Sales'].mean().sort_values(ascending=False)
    
    plt.figure(figsize=(12, 8))
    bars = plt.bar(range(len(store_avg)), store_avg.values, color='#A23B72')
    plt.title('Average Weekly Sales by Store', fontsize=16, pad=20)
    plt.xlabel('Store', fontsize=12)
    plt.ylabel('Average Sales ($)', fontsize=12)
    plt.xticks(range(0, len(store_avg), max(1, len(store_avg)//20)))  # Limit x-axis labels
    
    return save_plot_to_base64()

def plot_holiday_impact(df):
    """Create box plot comparing sales during holidays vs regular days"""
    plt.figure(figsize=(8, 6))
    sns.boxplot(data=df, x='Holiday_Flag', y='Weekly_Sales', palette=['#F18F01', '#C73E1D'])
    plt.title('Sales Distribution: Holiday vs Non-Holiday Weeks', fontsize=16, pad=20)
    plt.xlabel('Holiday Flag (0=Regular, 1=Holiday)', fontsize=12)
    plt.ylabel('Weekly Sales ($)', fontsize=12)
    
    return save_plot_to_base64()

def plot_correlation_heatmap(df):
    """Create correlation heatmap of numerical variables"""
    # Select numerical columns
    numerical_cols = ['Weekly_Sales', 'Temperature', 'Fuel_Price', 'CPI', 'Unemployment']
    corr_data = df[numerical_cols].corr()
    
    plt.figure(figsize=(10, 8))
    # Improve the heatmap with better formatting
    sns.heatmap(corr_data, 
                annot=True, 
                cmap='RdYlBu_r', 
                center=0, 
                square=True, 
                fmt='.3f',  # Increased precision to 3 decimal places
                cbar_kws={"shrink": .8},
                linewidths=0.5,  # Add lines between cells
                linecolor='white')
    plt.title('Correlation Matrix of Numerical Variables', fontsize=16, pad=20)
    
    return save_plot_to_base64()

def plot_sales_distribution(df):
    """Create histogram of sales distribution"""
    plt.figure(figsize=(10, 6))
    plt.hist(df['Weekly_Sales'], bins=50, color='#2E86AB', alpha=0.7, edgecolor='black', linewidth=0.5)
    plt.title('Distribution of Weekly Sales', fontsize=16, pad=20)
    plt.xlabel('Weekly Sales ($)', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.grid(True, alpha=0.3)
    
    return save_plot_to_base64()

def main():
    # Define file paths
    data_path = '/Users/simonwang/Documents/Usage/MathAI/MscMinicourse/Data/Walmart2.csv'
    output_dir = '/Users/simonwang/Documents/Usage/MathAI/MscMinicourse/Module1_InputProcessOutput/visual'
    html_output_path = os.path.join(output_dir, 'walmart_visualization_report.html')
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Load data
    print("Loading data...")
    df = load_and_prepare_data(data_path)
    print(f"Loaded {len(df)} records")
    
    # Generate plots
    print("Generating visualizations...")
    plots_data = []
    
    # 1. Sales over time
    img1 = plot_sales_over_time(df)
    plots_data.append({
        'title': '1. Total Weekly Sales Over Time',
        'description': 'This time series plot shows the total weekly sales across all Walmart stores over time. Trends, seasonal patterns, and anomalies can be observed in this visualization.',
        'image': img1
    })
    
    # 2. Sales by store
    img2 = plot_sales_by_store(df)
    plots_data.append({
        'title': '2. Average Weekly Sales by Store',
        'description': 'This bar chart displays the average weekly sales for each store, sorted from highest to lowest. It helps identify the best and worst performing stores.',
        'image': img2
    })
    
    # 3. Holiday impact
    img3 = plot_holiday_impact(df)
    plots_data.append({
        'title': '3. Sales Distribution: Holiday vs Non-Holiday Weeks',
        'description': 'This box plot compares the distribution of weekly sales during holiday weeks versus regular weeks. It shows how holidays impact sales volume and variability.',
        'image': img3
    })
    
    # 4. Correlation heatmap
    img4 = plot_correlation_heatmap(df)
    plots_data.append({
        'title': '4. Correlation Matrix of Numerical Variables',
        'description': 'This heatmap shows the correlation coefficients between numerical variables in the dataset. Red indicates positive correlation, blue indicates negative correlation, and intensity represents strength.',
        'image': img4
    })
    
    # 5. Sales distribution
    img5 = plot_sales_distribution(df)
    plots_data.append({
        'title': '5. Distribution of Weekly Sales',
        'description': 'This histogram shows the frequency distribution of weekly sales values. The shape of the distribution can reveal patterns such as skewness or multiple modes.',
        'image': img5
    })
    
    # Create HTML report
    print("Creating HTML report...")
    html_content = create_html_report(plots_data)
    
    # Save HTML report
    with open(html_output_path, 'w') as f:
        f.write(html_content)
    
    print(f"Visualization report saved to: {html_output_path}")

if __name__ == "__main__":
    main()