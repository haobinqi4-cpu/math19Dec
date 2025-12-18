#!/usr/bin/env python3
"""
Generate an enhanced heatmap with better visibility for correlation values.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime

def load_and_prepare_data(filepath):
    """Load and prepare the Walmart dataset"""
    df = pd.read_csv(filepath)
    
    # Convert date column to datetime (day-first format)
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
    
    # Sort by date for time series analysis
    df = df.sort_values('Date')
    
    return df

def plot_enhanced_correlation_heatmap(df):
    """Create an enhanced correlation heatmap with better visibility"""
    # Select numerical columns
    numerical_cols = ['Weekly_Sales', 'Temperature', 'Fuel_Price', 'CPI', 'Unemployment']
    corr_data = df[numerical_cols].corr()
    
    # Create figure with larger size
    plt.figure(figsize=(14, 12))
    
    # Create mask for upper triangle (optional, for cleaner look)
    mask = np.triu(np.ones_like(corr_data, dtype=bool))
    
    # Create heatmap with enhancements for better number visibility
    heatmap = sns.heatmap(corr_data, 
                          annot=True, 
                          cmap='RdYlBu_r', 
                          center=0, 
                          square=True, 
                          fmt='.3f',  # 3 decimal places
                          cbar_kws={"shrink": .8, "label": "Correlation Coefficient"},
                          linewidths=2,  # Thicker lines between cells
                          linecolor='white',
                          annot_kws={"size": 16, "weight": "bold"},  # Larger, bold annotation text
                          cbar=True,
                          mask=None)  # Show full matrix
    
    # Customize labels
    plt.title('Correlation Matrix of Numerical Variables\n(Walmart Sales Dataset)', 
              fontsize=20, pad=25, weight='bold')
    plt.xlabel('', fontsize=14)
    plt.ylabel('', fontsize=14)
    
    # Increase tick label size
    plt.xticks(fontsize=14, rotation=45)
    plt.yticks(fontsize=14, rotation=0)
    
    # Adjust colorbar
    cbar = heatmap.collections[0].colorbar
    cbar.ax.tick_params(labelsize=12)
    cbar.set_label('Correlation Coefficient', fontsize=14)
    
    # Adjust layout
    plt.tight_layout()
    
    return plt

def main():
    # Define file paths
    data_path = '/Users/simonwang/Documents/Usage/MathAI/MscMinicourse/Data/Walmart2.csv'
    output_path = '/Users/simonwang/Documents/Usage/MathAI/MscMinicourse/Module1_InputProcessOutput/visual/enhanced_correlation_heatmap.png'
    
    # Load data
    print("Loading data...")
    df = load_and_prepare_data(data_path)
    print(f"Loaded {len(df)} records")
    
    # Generate enhanced heatmap
    print("Generating enhanced correlation heatmap...")
    plt_obj = plot_enhanced_correlation_heatmap(df)
    
    # Save the heatmap image
    plt_obj.savefig(output_path, dpi=300, bbox_inches='tight')
    plt_obj.close()
    
    print(f"Enhanced heatmap saved to: {output_path}")
    
    # Also save a zoomable SVG version
    svg_path = output_path.replace('.png', '.svg')
    plt_obj = plot_enhanced_correlation_heatmap(df)
    plt_obj.savefig(svg_path, format='svg', bbox_inches='tight')
    plt_obj.close()
    
    print(f"SVG version saved to: {svg_path}")

if __name__ == "__main__":
    main()