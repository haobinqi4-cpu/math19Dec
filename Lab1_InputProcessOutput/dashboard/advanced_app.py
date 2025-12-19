"""
Advanced Interactive Dashboard for Walmart Sales Data Analysis
Includes multiple chart types, correlation analysis, and time series visualization.
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
app = dash.Dash(__name__, suppress_callback_exceptions=True)
app.title = "Advanced Walmart Sales Data Explorer"

# Load data
df = load_data()

# Get column names for dropdown options
numerical_columns = ['Weekly_Sales', 'Temperature', 'Fuel_Price', 'CPI', 'Unemployment']
categorical_columns = ['Store', 'Holiday_Flag', 'District']

# App layout
app.layout = html.Div([
    # Header
    html.Div([
        html.H1("Advanced Walmart Sales Data Explorer", 
                style={'textAlign': 'center', 'color': '#2c3e50', 'marginBottom': '10px'}),
        html.P("Comprehensive analysis of relationships among different factors in the Walmart sales dataset", 
               style={'textAlign': 'center', 'color': '#7f8c8d', 'fontSize': '18px'})
    ], style={'backgroundColor': '#ecf0f1', 'padding': '20px', 'borderRadius': '10px', 'marginBottom': '20px'}),
    
    # Tabs for different analysis views
    dcc.Tabs(id='tabs', value='explorer', children=[
        dcc.Tab(label='Interactive Explorer', value='explorer', children=[
            html.Div([
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
                                    {'label': 'Box Plot', 'value': 'box'},
                                    {'label': '3D Scatter', 'value': '3d_scatter'}
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
                    html.H2("Variable Summary", style={'color': '#3498db', 'marginBottom': '15px'}),
                    html.Div(id='data-summary')
                ], style={'backgroundColor': '#f8f9fa', 'padding': '20px', 'borderRadius': '10px'}),
            ], style={'padding': '20px'})
        ]),
        
        dcc.Tab(label='Correlation Analysis', value='correlation', children=[
            html.Div([
                html.H2("Correlation Matrix", style={'color': '#3498db', 'textAlign': 'center'}),
                html.Div([
                    dcc.Graph(id='correlation-heatmap', style={'height': '600px'})
                ]),
                html.Div(id='correlation-insights', 
                        style={'backgroundColor': '#f8f9fa', 'padding': '20px', 'borderRadius': '10px', 'marginTop': '20px'})
            ], style={'padding': '20px'})
        ]),
        
        dcc.Tab(label='Time Series Analysis', value='timeseries', children=[
            html.Div([
                html.H2("Time Series Analysis", style={'color': '#3498db', 'textAlign': 'center'}),
                html.Div([
                    html.Label("Select Variable:", style={'fontWeight': 'bold'}),
                    dcc.Dropdown(
                        id='ts-variable-dropdown',
                        options=[{'label': col, 'value': col} for col in numerical_columns],
                        value='Weekly_Sales',
                        clearable=False
                    )
                ], style={'marginBottom': '20px', 'width': '300px'}),
                html.Div([
                    dcc.Graph(id='time-series-chart', style={'height': '500px'})
                ]),
                html.Div([
                    dcc.Graph(id='seasonal-decomposition', style={'height': '400px'})
                ])
            ], style={'padding': '20px'})
        ]),
        
        dcc.Tab(label='Data Overview', value='data', children=[
            html.Div([
                html.H2("Dataset Information", style={'color': '#3498db'}),
                html.Div([
                    html.H3("Dataset Shape"),
                    html.P(f"Rows: {len(df)}, Columns: {len(df.columns)}"),
                    html.H3("Column Names"),
                    html.Ul([html.Li(col) for col in df.columns]),
                    html.H3("Data Types"),
                    html.Ul([html.Li(f"{col}: {dtype}") for col, dtype in df.dtypes.items()]),
                ], style={'backgroundColor': '#f8f9fa', 'padding': '20px', 'borderRadius': '10px', 'marginBottom': '20px'}),
                
                html.H2("Sample Data", style={'color': '#3498db'}),
                dash_table.DataTable(
                    id='data-table',
                    columns=[{"name": i, "id": i} for i in df.columns],
                    data=df.head(15).to_dict('records'),
                    style_table={'overflowX': 'auto'},
                    style_cell={
                        'height': 'auto',
                        'minWidth': '100px', 'width': '100px', 'maxWidth': '180px',
                        'whiteSpace': 'normal'
                    },
                    page_size=15,
                )
            ], style={'padding': '20px'})
        ]),
    ]),
])

# Callback to update the main chart based on user selections
@callback(
    Output('main-chart', 'figure'),
    [Input('x-axis-dropdown', 'value'),
     Input('y-axis-dropdown', 'value'),
     Input('chart-type-dropdown', 'value'),
     Input('color-dropdown', 'value'),
     Input('size-dropdown', 'value')]
)
def update_main_chart(x_axis, y_axis, chart_type, color_by, size_by):
    """Update the main chart based on user selections"""
    # Handle the case where color_by or size_by is 'None'
    color_col = None if color_by == 'None' else color_by
    size_col = None if size_by == 'None' else size_by
    
    # Create different chart types based on selection
    if chart_type == 'scatter':
        if size_col:
            fig = px.scatter(df, x=x_axis, y=y_axis, color=color_col, size=size_col,
                           title=f'{y_axis} vs {x_axis}',
                           hover_data=['Date', 'Store'])
        else:
            fig = px.scatter(df, x=x_axis, y=y_axis, color=color_col,
                           title=f'{y_axis} vs {x_axis}',
                           hover_data=['Date', 'Store'])
    
    elif chart_type == 'line':
        # For line chart, we'll aggregate data by date
        if color_col:
            agg_data = df.groupby([df['Date'].dt.date, color_col]).agg({x_axis: 'mean', y_axis: 'mean'}).reset_index()
            fig = px.line(agg_data, x=x_axis, y=y_axis, color=color_col,
                         title=f'{y_axis} vs {x_axis} (Aggregated by Date)')
        else:
            agg_data = df.groupby(df['Date'].dt.date).agg({x_axis: 'mean', y_axis: 'mean'}).reset_index()
            fig = px.line(agg_data, x=x_axis, y=y_axis,
                         title=f'{y_axis} vs {x_axis} (Aggregated by Date)')
    
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
    
    elif chart_type == '3d_scatter':
        z_axis = 'Weekly_Sales'  # Default Z axis
        if x_axis != 'Weekly_Sales' and y_axis != 'Weekly_Sales':
            z_axis = 'Weekly_Sales'
        elif x_axis != 'Temperature' and y_axis != 'Temperature':
            z_axis = 'Temperature'
        
        if color_col:
            fig = px.scatter_3d(df, x=x_axis, y=y_axis, z=z_axis, color=color_col,
                               title=f'3D View: {x_axis} vs {y_axis} vs {z_axis}')
        else:
            fig = px.scatter_3d(df, x=x_axis, y=y_axis, z=z_axis,
                               title=f'3D View: {x_axis} vs {y_axis} vs {z_axis}')
    
    # Update layout
    fig.update_layout(
        plot_bgcolor='#ffffff',
        paper_bgcolor='#ffffff',
        font=dict(size=14),
        title_font=dict(size=18, family="Arial Black")
    )
    
    return fig

# Callback to update data summary
@callback(
    Output('data-summary', 'children'),
    [Input('x-axis-dropdown', 'value'),
     Input('y-axis-dropdown', 'value')]
)
def update_summary(x_axis, y_axis):
    """Update the data summary section"""
    # Get basic statistics for both selected columns
    x_stats = df[x_axis].describe()
    y_stats = df[y_axis].describe()
    
    # Get correlation between the two variables
    correlation = df[x_axis].corr(df[y_axis])
    
    # Get additional insights
    x_missing = df[x_axis].isnull().sum()
    y_missing = df[y_axis].isnull().sum()
    
    summary_html = html.Div([
        html.H3("Variable Statistics", style={'color': '#2c3e50'}),
        html.Div([
            html.Div([
                html.H4(f"{x_axis}", style={'color': '#3498db'}),
                html.Ul([
                    html.Li(f"Count: {int(x_stats['count'])}"),
                    html.Li(f"Mean: {x_stats['mean']:.2f}"),
                    html.Li(f"Std Dev: {x_stats['std']:.2f}"),
                    html.Li(f"Min: {x_stats['min']:.2f}"),
                    html.Li(f"Max: {x_stats['max']:.2f}"),
                    html.Li(f"Missing Values: {x_missing}")
                ])
            ], className="six columns"),
            
            html.Div([
                html.H4(f"{y_axis}", style={'color': '#3498db'}),
                html.Ul([
                    html.Li(f"Count: {int(y_stats['count'])}"),
                    html.Li(f"Mean: {y_stats['mean']:.2f}"),
                    html.Li(f"Std Dev: {y_stats['std']:.2f}"),
                    html.Li(f"Min: {y_stats['min']:.2f}"),
                    html.Li(f"Max: {y_stats['max']:.2f}"),
                    html.Li(f"Missing Values: {y_missing}")
                ])
            ], className="six columns"),
        ], className="row"),
        
        html.Div([
            html.H4("Relationship Insights", style={'color': '#27ae60', 'marginTop': '15px'}),
            html.Ul([
                html.Li(f"Correlation between {x_axis} and {y_axis}: {correlation:.3f}"),
                html.Li(f"Relationship strength: {get_relationship_strength(abs(correlation))}"),
                html.Li(f"Relationship direction: {get_relationship_direction(correlation)}")
            ])
        ])
    ])
    
    return summary_html

def get_relationship_strength(correlation):
    """Describe the strength of a correlation"""
    if correlation >= 0.7:
        return "Strong"
    elif correlation >= 0.3:
        return "Moderate"
    elif correlation >= 0.1:
        return "Weak"
    else:
        return "Very weak or no linear relationship"

def get_relationship_direction(correlation):
    """Describe the direction of a correlation"""
    if correlation > 0:
        return "Positive (as one increases, the other tends to increase)"
    elif correlation < 0:
        return "Negative (as one increases, the other tends to decrease)"
    else:
        return "No linear relationship"

# Callback to update correlation heatmap
@callback(
    [Output('correlation-heatmap', 'figure'),
     Output('correlation-insights', 'children')],
    Input('tabs', 'value')
)
def update_correlation_analysis(tab):
    """Update the correlation analysis tab"""
    if tab != 'correlation':
        # Return empty figures if not on correlation tab
        return {}, ""
    
    # Calculate correlation matrix
    corr_data = df[numerical_columns].corr()
    
    # Create heatmap
    fig = px.imshow(corr_data, 
                    text_auto='.3f',
                    aspect="auto",
                    color_continuous_scale='RdBu_r',
                    title='Correlation Matrix of Numerical Variables')
    
    fig.update_layout(
        plot_bgcolor='#ffffff',
        paper_bgcolor='#ffffff',
        font=dict(size=14),
        title_font=dict(size=18, family="Arial Black")
    )
    
    # Generate insights
    insights = generate_correlation_insights(corr_data)
    
    insights_html = html.Div([
        html.H3("Key Correlation Insights", style={'color': '#2c3e50'}),
        html.Ul([html.Li(insight) for insight in insights])
    ])
    
    return fig, insights_html

def generate_correlation_insights(corr_data):
    """Generate insights from correlation data"""
    insights = []
    
    # Find strongest correlations
    corr_pairs = []
    for i in range(len(corr_data.columns)):
        for j in range(i+1, len(corr_data.columns)):
            corr_val = corr_data.iloc[i, j]
            corr_pairs.append((corr_data.columns[i], corr_data.columns[j], abs(corr_val), corr_val))
    
    # Sort by absolute correlation
    corr_pairs.sort(key=lambda x: x[2], reverse=True)
    
    # Report top correlations
    for i, (var1, var2, abs_corr, corr) in enumerate(corr_pairs[:5]):
        direction = "positive" if corr > 0 else "negative"
        strength = get_relationship_strength(abs_corr).lower()
        insights.append(f"{var1} and {var2} have a {strength} {direction} correlation ({corr:.3f})")
    
    # Check for any strong correlations with Weekly_Sales
    sales_corr = corr_data['Weekly_Sales'].drop('Weekly_Sales')
    strong_sales_corr = sales_corr[abs(sales_corr) > 0.1]
    
    if len(strong_sales_corr) > 0:
        insights.append("Variables with notable correlation to Weekly Sales:")
        for var, corr in strong_sales_corr.items():
            insights.append(f"  • {var}: {corr:.3f}")
    else:
        insights.append("No variables show strong correlation (>0.1) with Weekly Sales")
    
    return insights

# Callback to update time series chart
@callback(
    [Output('time-series-chart', 'figure'),
     Output('seasonal-decomposition', 'figure')],
    [Input('ts-variable-dropdown', 'value'),
     Input('tabs', 'value')]
)
def update_time_series(variable, tab):
    """Update the time series analysis tab"""
    if tab != 'timeseries':
        # Return empty figures if not on timeseries tab
        return {}, {}
    
    # Aggregate data by date
    ts_data = df.groupby(df['Date'].dt.date)[variable].mean().reset_index()
    ts_data.columns = ['Date', variable]
    
    # Create time series line chart
    fig_ts = px.line(ts_data, x='Date', y=variable, title=f'Time Series: {variable}')
    fig_ts.update_layout(
        plot_bgcolor='#ffffff',
        paper_bgcolor='#ffffff',
        font=dict(size=14),
        title_font=dict(size=18, family="Arial Black")
    )
    
    # Create a simple trend visualization
    # Add moving average
    ts_data['MA_4'] = ts_data[variable].rolling(window=4).mean()
    ts_data['MA_12'] = ts_data[variable].rolling(window=12).mean()
    
    fig_trend = go.Figure()
    fig_trend.add_trace(go.Scatter(x=ts_data['Date'], y=ts_data[variable], mode='lines', name=variable, opacity=0.7))
    fig_trend.add_trace(go.Scatter(x=ts_data['Date'], y=ts_data['MA_4'], mode='lines', name='4-week MA'))
    fig_trend.add_trace(go.Scatter(x=ts_data['Date'], y=ts_data['MA_12'], mode='lines', name='12-week MA'))
    
    fig_trend.update_layout(
        title=f'{variable} with Moving Averages',
        plot_bgcolor='#ffffff',
        paper_bgcolor='#ffffff',
        font=dict(size=14),
        title_font=dict(size=18, family="Arial Black")
    )
    
    return fig_ts, fig_trend

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, port=8051)