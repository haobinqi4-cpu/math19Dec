"""
Simple Dashboard for Walmart Sales Data Analysis
Using Flask and Plotly for a lightweight solution.
"""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from flask import Flask, render_template, request, jsonify
import json
import plotly
import numpy as np
from datetime import datetime

# Load and prepare data
def load_data():
    """Load and prepare the Walmart dataset"""
    df = pd.read_csv('/Users/simonwang/Documents/Usage/MathAI/MscMinicourse/Data/Walmart2.csv')
    # Convert date column to datetime (day-first format)
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
    return df

# Initialize Flask app
app = Flask(__name__)

# Load data
df = load_data()

# Get column names for dropdown options
numerical_columns = ['Weekly_Sales', 'Temperature', 'Fuel_Price', 'CPI', 'Unemployment']
categorical_columns = ['Store', 'Holiday_Flag', 'District']

@app.route('/')
def index():
    """Main dashboard page"""
    return render_template('dashboard.html', 
                         numerical_columns=numerical_columns,
                         categorical_columns=categorical_columns)

@app.route('/get_chart', methods=['POST'])
def get_chart():
    """Generate chart based on user selections"""
    data = request.get_json()
    
    x_axis = data.get('x_axis', 'Temperature')
    y_axis = data.get('y_axis', 'Weekly_Sales')
    chart_type = data.get('chart_type', 'scatter')
    color_by = data.get('color_by', 'None')
    size_by = data.get('size_by', 'None')
    
    # Handle the case where color_by or size_by is 'None'
    color_col = None if color_by == 'None' else color_by
    size_col = None if size_by == 'None' else size_by
    
    # Create different chart types based on selection
    if chart_type == 'scatter':
        if size_col and size_col != 'None':
            fig = px.scatter(df, x=x_axis, y=y_axis, color=color_col, size=size_col,
                           title=f'{y_axis} vs {x_axis}')
        else:
            fig = px.scatter(df, x=x_axis, y=y_axis, color=color_col,
                           title=f'{y_axis} vs {x_axis}')
    
    elif chart_type == 'line':
        # For line chart, we'll aggregate data by date
        if color_col and color_col != 'None':
            agg_data = df.groupby([df['Date'].dt.date, color_col]).agg({x_axis: 'mean', y_axis: 'mean'}).reset_index()
            fig = px.line(agg_data, x=x_axis, y=y_axis, color=color_col,
                         title=f'{y_axis} vs {x_axis} (Time Series)')
        else:
            agg_data = df.groupby(df['Date'].dt.date).agg({x_axis: 'mean', y_axis: 'mean'}).reset_index()
            fig = px.line(agg_data, x=x_axis, y=y_axis,
                         title=f'{y_axis} vs {x_axis} (Time Series)')
    
    elif chart_type == 'bar':
        # For bar chart, we'll group by the x-axis variable if it's categorical or discretized
        if color_col and color_col != 'None':
            fig = px.bar(df, x=x_axis, y=y_axis, color=color_col,
                        title=f'Average {y_axis} by {x_axis}')
        else:
            fig = px.bar(df, x=x_axis, y=y_axis,
                        title=f'Average {y_axis} by {x_axis}')
    
    elif chart_type == 'histogram':
        fig = px.histogram(df, x=x_axis, color=color_col,
                          title=f'Distribution of {x_axis}')
    
    elif chart_type == 'box':
        fig = px.box(df, x=x_axis, y=y_axis, color=color_col,
                    title=f'Distribution of {y_axis} by {x_axis}')
    
    # Convert the plotly figure to JSON
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

@app.route('/get_summary', methods=['POST'])
def get_summary():
    """Get summary statistics for selected columns"""
    data = request.get_json()
    x_axis = data.get('x_axis', 'Temperature')
    y_axis = data.get('y_axis', 'Weekly_Sales')
    
    # Get basic statistics for both selected columns
    x_stats = df[x_axis].describe()
    y_stats = df[y_axis].describe()
    
    # Get correlation between the two variables
    correlation = df[x_axis].corr(df[y_axis])
    
    # Format the summary as HTML
    summary_html = f"""
    <div>
        <h3>Variable Statistics</h3>
        <div style="display: flex;">
            <div style="width: 50%;">
                <h4>{x_axis}</h4>
                <ul>
                    <li>Count: {int(x_stats['count'])}</li>
                    <li>Mean: {x_stats['mean']:.2f}</li>
                    <li>Std Dev: {x_stats['std']:.2f}</li>
                    <li>Min: {x_stats['min']:.2f}</li>
                    <li>Max: {x_stats['max']:.2f}</li>
                </ul>
            </div>
            <div style="width: 50%;">
                <h4>{y_axis}</h4>
                <ul>
                    <li>Count: {int(y_stats['count'])}</li>
                    <li>Mean: {y_stats['mean']:.2f}</li>
                    <li>Std Dev: {y_stats['std']:.2f}</li>
                    <li>Min: {y_stats['min']:.2f}</li>
                    <li>Max: {y_stats['max']:.2f}</li>
                </ul>
            </div>
        </div>
        <div>
            <h4>Relationship Insights</h4>
            <ul>
                <li>Correlation between {x_axis} and {y_axis}: {correlation:.3f}</li>
            </ul>
        </div>
    </div>
    """
    
    return summary_html

if __name__ == '__main__':
    app.run(debug=True, port=8050)