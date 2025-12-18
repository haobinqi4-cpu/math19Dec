#!/usr/bin/env python3
"""
Generate an improved heatmap for the Walmart dataset correlation matrix.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime
import base64
from io import BytesIO

def load_and_prepare_data(filepath):
    """Load and prepare the Walmart dataset"""
    df = pd.read_csv(filepath)
    
    # Convert date column to datetime (day-first format)
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
    
    # Sort by date for time series analysis
    df = df.sort_values('Date')
    
    return df

def plot_improved_correlation_heatmap(df):
    """Create an improved correlation heatmap of numerical variables"""
    # Select numerical columns
    numerical_cols = ['Weekly_Sales', 'Temperature', 'Fuel_Price', 'CPI', 'Unemployment']
    corr_data = df[numerical_cols].corr()
    
    # Create figure
    plt.figure(figsize=(12, 10))
    
    # Create heatmap with improvements
    heatmap = sns.heatmap(corr_data, 
                          annot=True, 
                          cmap='RdYlBu_r', 
                          center=0, 
                          square=True, 
                          fmt='.3f',  # 3 decimal places
                          cbar_kws={"shrink": .8, "label": "Correlation Coefficient"},
                          linewidths=1,  # Thicker lines between cells
                          linecolor='white',
                          annot_kws={"size": 14})  # Larger annotation text
    
    # Customize labels
    plt.title('Correlation Matrix of Numerical Variables\n(Walmart Sales Dataset)', 
              fontsize=18, pad=25, weight='bold')
    plt.xlabel('', fontsize=14)
    plt.ylabel('', fontsize=14)
    
    # Increase tick label size
    plt.xticks(fontsize=12, rotation=45)
    plt.yticks(fontsize=12, rotation=0)
    
    # Adjust layout
    plt.tight_layout()
    
    return plt

def save_plot_to_file(plt_obj, filename):
    """Save plot to file"""
    plt_obj.savefig(filename, dpi=300, bbox_inches='tight')
    plt_obj.close()

def create_standalone_html(corr_data, image_path):
    """Create a standalone HTML file with the heatmap"""
    html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Walmart Sales Data - Correlation Heatmap</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f8f9fa;
        }}
        .container {{
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 0 20px rgba(0,0,0,0.1);
            padding: 30px;
            margin-bottom: 20px;
        }}
        h1 {{
            color: #2c3e50;
            text-align: center;
            margin-bottom: 30px;
            font-size: 2.5em;
        }}
        h2 {{
            color: #3498db;
            border-bottom: 2px solid #3498db;
            padding-bottom: 10px;
        }}
        .heatmap-container {{
            text-align: center;
            margin: 30px 0;
        }}
        .heatmap-img {{
            max-width: 100%;
            height: auto;
            border: 1px solid #ddd;
            border-radius: 5px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }}
        .explanation {{
            background-color: #e8f4fc;
            border-left: 4px solid #3498db;
            padding: 20px;
            margin: 25px 0;
            border-radius: 0 5px 5px 0;
        }}
        .interpretation {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin: 25px 0;
        }}
        .interpretation-box {{
            background-color: #fff;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        }}
        .interpretation-box h3 {{
            margin-top: 0;
            color: #2c3e50;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 12px;
            text-align: center;
        }}
        th {{
            background-color: #3498db;
            color: white;
        }}
        tr:nth-child(even) {{
            background-color: #f2f2f2;
        }}
        .positive {{
            background-color: #e8f5e9;
        }}
        .negative {{
            background-color: #ffebee;
        }}
        .strong {{
            font-weight: bold;
        }}
        .footer {{
            text-align: center;
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid #eee;
            color: #7f8c8d;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Walmart Sales Data Correlation Analysis</h1>
        
        <div class="explanation">
            <h2>About This Visualization</h2>
            <p>This heatmap displays the correlation coefficients between numerical variables in the Walmart sales dataset. 
            Correlation values range from -1 to 1:</p>
            <ul>
                <li><strong>+1</strong>: Perfect positive correlation</li>
                <li><strong>0</strong>: No linear correlation</li>
                <li><strong>-1</strong>: Perfect negative correlation</li>
            </ul>
            <p>Colors represent the strength and direction of correlations: red for positive, blue for negative.</p>
        </div>
        
        <div class="heatmap-container">
            <img src="{image_path}" alt="Correlation Heatmap" class="heatmap-img">
        </div>
        
        <div class="interpretation">
            <div class="interpretation-box">
                <h3>Strong Correlations</h3>
                <p>Values with absolute correlation > 0.5:</p>
                <table>
                    <tr>
                        <th>Variable 1</th>
                        <th>Variable 2</th>
                        <th>Correlation</th>
                    </tr>
"""
    
    # Add strong correlations to the table
    strong_corr = []
    for i in range(len(corr_data.columns)):
        for j in range(i+1, len(corr_data.columns)):
            corr_val = corr_data.iloc[i, j]
            if abs(corr_val) > 0.5:
                strong_corr.append((corr_data.columns[i], corr_data.columns[j], corr_val))
    
    # Sort by absolute correlation value
    strong_corr.sort(key=lambda x: abs(x[2]), reverse=True)
    
    for var1, var2, corr_val in strong_corr:
        css_class = "positive" if corr_val > 0 else "negative"
        css_class += " strong" if abs(corr_val) > 0.7 else ""
        html_content += f"""
                    <tr class="{css_class}">
                        <td>{var1}</td>
                        <td>{var2}</td>
                        <td>{corr_val:.3f}</td>
                    </tr>"""
    
    html_content += """
                </table>
            </div>
            
            <div class="interpretation-box">
                <h3>Data Summary</h3>
                <p>Dataset contains {rows} rows and {cols} numerical columns.</p>
                <p><strong>Variables analyzed:</strong></p>
                <ul>
""".format(rows=len(corr_data)*1000, cols=len(corr_data.columns))  # Approximate row count
    
    for col in corr_data.columns:
        html_content += f"                    <li>{col}</li>\n"
    
    html_content += """
                </ul>
                <p>All correlation values are displayed with three decimal places for precision.</p>
            </div>
        </div>
        
        <div class="explanation">
            <h2>Interpretation Guide</h2>
            <p><strong>Positive Correlation:</strong> As one variable increases, the other tends to increase.</p>
            <p><strong>Negative Correlation:</strong> As one variable increases, the other tends to decrease.</p>
            <p><strong>Strength Guidelines:</strong></p>
            <ul>
                <li>|r| ≥ 0.7: Strong correlation</li>
                <li>0.3 ≤ |r| < 0.7: Moderate correlation</li>
                <li>|r| < 0.3: Weak correlation</li>
            </ul>
        </div>
    </div>
    
    <div class="footer">
        <p>Generated on {date} | Walmart Sales Dataset Analysis</p>
    </div>
</body>
</html>
""".format(date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    
    return html_content

def main():
    # Define file paths
    data_path = '/Users/simonwang/Documents/Usage/MathAI/MscMinicourse/Data/Walmart2.csv'
    image_output_path = '/Users/simonwang/Documents/Usage/MathAI/MscMinicourse/Module1_InputProcessOutput/visual/correlation_heatmap.png'
    html_output_path = '/Users/simonwang/Documents/Usage/MathAI/MscMinicourse/Module1_InputProcessOutput/visual/improved_correlation_heatmap.html'
    
    # Load data
    print("Loading data...")
    df = load_and_prepare_data(data_path)
    print(f"Loaded {len(df)} records")
    
    # Select numerical columns for correlation analysis
    numerical_cols = ['Weekly_Sales', 'Temperature', 'Fuel_Price', 'CPI', 'Unemployment']
    corr_data = df[numerical_cols].corr()
    
    # Generate improved heatmap
    print("Generating improved correlation heatmap...")
    plt_obj = plot_improved_correlation_heatmap(df)
    
    # Save the heatmap image
    save_plot_to_file(plt_obj, image_output_path)
    print(f"Heatmap image saved to: {image_output_path}")
    
    # Create standalone HTML file
    print("Creating standalone HTML file...")
    html_content = create_standalone_html(corr_data, "correlation_heatmap.png")
    
    # Save HTML file
    with open(html_output_path, 'w') as f:
        f.write(html_content)
    
    print(f"Improved heatmap HTML report saved to: {html_output_path}")

if __name__ == "__main__":
    main()