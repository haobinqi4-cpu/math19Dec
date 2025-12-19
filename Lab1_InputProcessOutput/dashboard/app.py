"""
Interactive Dashboard for Walmart Sales Data Analysis
Allows users to explore relationships among different factors using various chart types.
"""

import dash
from dash import dcc, html, Input, Output, callback, dash_table
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from datetime import datetime

# Load and prepare data
def load_data():
    """Load and prepare the Walmart dataset"""
    df = pd.read_csv('/Users/simonwang/Documents/Usage/MathAI/MscMinicourse/Data/Walmart2.csv')
    # Convert date column to datetime (day-first format)
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
    return df

# Initialize the app
app = dash.Dash(__name__)
app.title = "Walmart Sales Data Explorer"

# Load data
df = load_data()

# Get column names for dropdown options
numerical_columns = ['Weekly_Sales', 'Temperature', 'Fuel_Price', 'CPI', 'Unemployment']
categorical_columns = ['Store', 'Holiday_Flag', 'District']

# App layout
app.layout = html.Div([
    # Header
    html.Div([
        html.H1("Walmart Sales Data Explorer", 
                style={'textAlign': 'center', 'color': '#2c3e50', 'marginBottom': '10px'}),
        html.P("Explore relationships among different factors in the Walmart sales dataset", 
               style={'textAlign': 'center', 'color': '#7f8c8d', 'fontSize': '18px'})
    ], style={'backgroundColor': '#ecf0f1', 'padding': '20px', 'borderRadius': '10px', 'marginBottom': '20px'}),
    
    # Controls section
    html.Div([
        html.H2("Chart Controls", style={'color': '#3498db', 'marginBottom': '15px'}),
        
        html.Div([
            html.Div([
                html.Label("X-Axis Variable:", style={'fontWeight': 'bold'}),
                dcc.Dropdown(
                    id='x-axis-dropdown',
                    options=[{'label': col, 'value': col} for col in numerical_columns],
                    value='Temperature',
                    clearable=False
                )
            ], className="six columns"),
            
            html.Div([
                html.Label("Y-Axis Variable:", style={'fontWeight': 'bold'}),
                dcc.Dropdown(
                    id='y-axis-dropdown',
                    options=[{'label': col, 'value': col} for col in numerical_columns],
                    value='Weekly_Sales',
                    clearable=False
                )
            ], className="six columns"),
        ], className="row", style={'marginBottom': '20px'}),
        
        html.Div([
            html.Div([
                html.Label("Chart Type:", style={'fontWeight': 'bold'}),
                dcc.Dropdown(
                    id='chart-type-dropdown',
                    options=[
                        {'label': 'Scatter Plot', 'value': 'scatter'},
                        {'label': 'Line Chart', 'value': 'line'},
                        {'label': 'Bar Chart', 'value': 'bar'},
                        {'label': 'Histogram', 'value': 'histogram'},
                        {'label': 'Box Plot', 'value': 'box'}
                    ],
                    value='scatter',
                    clearable=False
                )
            ], className="four columns"),
            
            html.Div([
                html.Label("Color By:", style={'fontWeight': 'bold'}),
                dcc.Dropdown(
                    id='color-dropdown',
                    options=[{'label': 'None', 'value': 'None'}] + 
                            [{'label': col, 'value': col} for col in categorical_columns + numerical_columns],
                    value='None',
                    clearable=False
                )
            ], className="four columns"),
            
            html.Div([
                html.Label("Size By (Scatter only):", style={'fontWeight': 'bold'}),
                dcc.Dropdown(
                    id='size-dropdown',
                    options=[{'label': 'None', 'value': 'None'}] + 
                            [{'label': col, 'value': col} for col in numerical_columns],
                    value='None',
                    clearable=False
                )
            ], className="four columns"),
        ], className="row", style={'marginBottom': '20px'}),
    ], style={'backgroundColor': '#f8f9fa', 'padding': '20px', 'borderRadius': '10px', 'marginBottom': '20px'}),
    
    # Chart display
    html.Div([
        dcc.Graph(id='main-chart', style={'height': '600px'})
    ], style={'marginBottom': '20px'}),
    
    # Data summary
    html.Div([
        html.H2("Dataset Summary", style={'color': '#3498db', 'marginBottom': '15px'}),
        html.Div(id='data-summary')
    ], style={'backgroundColor': '#f8f9fa', 'padding': '20px', 'borderRadius': '10px', 'marginBottom': '20px'}),
    
    # Data table
    html.Div([
        html.H2("Sample Data", style={'color': '#3498db', 'marginBottom': '15px'}),
        dash_table.DataTable(
            id='data-table',
            columns=[{"name": i, "id": i} for i in df.columns],
            data=df.head(10).to_dict('records'),
            style_table={'overflowX': 'auto'},
            style_cell={
                'height': 'auto',
                'minWidth': '100px', 'width': '100px', 'maxWidth': '180px',
                'whiteSpace': 'normal'
            },
            page_size=10,
        )
    ], style={'backgroundColor': '#f8f9fa', 'padding': '20px', 'borderRadius': '10px'})
])

# Callback to update the chart based on user selections
@callback(
    Output('main-chart', 'figure'),
    [Input('x-axis-dropdown', 'value'),
     Input('y-axis-dropdown', 'value'),
     Input('chart-type-dropdown', 'value'),
     Input('color-dropdown', 'value'),
     Input('size-dropdown', 'value')]
)
def update_chart(x_axis, y_axis, chart_type, color_by, size_by):
    """Update the chart based on user selections"""
    # Handle the case where color_by or size_by is 'None'
    color_col = None if color_by == 'None' else color_by
    size_col = None if size_by == 'None' else size_by
    
    # Create different chart types based on selection
    if chart_type == 'scatter':
        if size_col:
            fig = px.scatter(df, x=x_axis, y=y_axis, color=color_col, size=size_col,
                           title=f'{y_axis} vs {x_axis}')
        else:
            fig = px.scatter(df, x=x_axis, y=y_axis, color=color_col,
                           title=f'{y_axis} vs {x_axis}')
    
    elif chart_type == 'line':
        # For line chart, we'll aggregate data by date
        if color_col:
            agg_data = df.groupby([df['Date'].dt.date, color_col]).agg({x_axis: 'mean', y_axis: 'mean'}).reset_index()
            fig = px.line(agg_data, x=x_axis, y=y_axis, color=color_col,
                         title=f'{y_axis} vs {x_axis} (Time Series)')
        else:
            agg_data = df.groupby(df['Date'].dt.date).agg({x_axis: 'mean', y_axis: 'mean'}).reset_index()
            fig = px.line(agg_data, x=x_axis, y=y_axis,
                         title=f'{y_axis} vs {x_axis} (Time Series)')
    
    elif chart_type == 'bar':
        # For bar chart, we'll group by the x-axis variable if it's categorical or discretized
        if color_col:
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
    
    # Update layout
    fig.update_layout(
        plot_bgcolor='#ffffff',
        paper_bgcolor='#ffffff',
        font=dict(size=14),
        title_font=dict(size=18, family="Arial Black"),
        xaxis_title=x_axis,
        yaxis_title=y_axis if chart_type != 'histogram' else 'Count'
    )
    
    return fig

# Callback to update data summary
@callback(
    Output('data-summary', 'children'),
    Input('x-axis-dropdown', 'value')
)
def update_summary(selected_column):
    """Update the data summary section"""
    # Get basic statistics for the selected column
    col_stats = df[selected_column].describe()
    
    # Get correlation with Weekly_Sales
    correlation = df[selected_column].corr(df['Weekly_Sales'])
    
    summary_html = html.Div([
        html.H3(f"Summary for {selected_column}", style={'color': '#2c3e50'}),
        html.Ul([
            html.Li(f"Count: {int(col_stats['count'])}"),
            html.Li(f"Mean: {col_stats['mean']:.2f}"),
            html.Li(f"Standard Deviation: {col_stats['std']:.2f}"),
            html.Li(f"Minimum: {col_stats['min']:.2f}"),
            html.Li(f"Maximum: {col_stats['max']:.2f}"),
            html.Li(f"Correlation with Weekly Sales: {correlation:.3f}")
        ], style={'fontSize': '16px'}),
        
        html.P("Use the controls above to explore relationships between different variables in the dataset.",
               style={'marginTop': '15px', 'fontStyle': 'italic'})
    ])
    
    return summary_html

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, port=8050)