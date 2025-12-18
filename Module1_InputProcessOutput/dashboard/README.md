# Walmart Sales Data Explorer Dashboard

An interactive dashboard for exploring relationships among different factors in the Walmart sales dataset.

## Features

- Interactive charts with multiple visualization options (scatter plots, line charts, bar charts, histograms, box plots)
- Dynamic selection of X and Y axes from numerical variables
- Color coding by categorical or numerical variables
- Size encoding for scatter plots
- Real-time updates based on user selections
- Data summary statistics
- Sample data table

## Variables Available

### Numerical Variables:
- **Weekly_Sales**: Total sales for the week
- **Temperature**: Average temperature during the week
- **Fuel_Price**: Fuel price during the week
- **CPI**: Consumer Price Index
- **Unemployment**: Unemployment rate

### Categorical Variables:
- **Store**: Store identifier
- **Holiday_Flag**: Indicates if the week is a holiday week (1) or not (0)
- **District**: District identifier

## Installation

1. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the dashboard:
```bash
python app.py
```

2. Open your web browser and go to `http://localhost:8050`

3. Use the dropdown menus to select:
   - X-axis variable
   - Y-axis variable
   - Chart type
   - Color coding variable
   - Size variable (for scatter plots)

4. The chart will update automatically based on your selections

## Chart Types

- **Scatter Plot**: Shows relationship between two numerical variables
- **Line Chart**: Displays trends over time (aggregated by date)
- **Bar Chart**: Compares average values across categories
- **Histogram**: Shows distribution of a single variable
- **Box Plot**: Displays distribution and outliers for different categories

## How It Works

The dashboard uses Plotly Dash to create an interactive web interface. When you make selections, callbacks update the chart in real-time. The data is loaded once when the application starts and then filtered/processed as needed for visualization.