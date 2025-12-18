# Module 2: Data.gov.hk API Access & Analysis

## Overview

This module teaches MSc Mathematics students how to programmatically access Hong Kong government open data using APIs, analyze the data using Python, and apply the Input-Process-Output (IPO) model from Module 1.

### Learning Objectives

By the end of this module, students will be able to:
1. Understand RESTful API concepts and HTTP requests
2. Access data.gov.hk datasets programmatically
3. Parse JSON responses and extract relevant data
4. Perform statistical analysis on government data
5. Apply IPO thinking to data pipelines
6. Create visualizations from API data

---

## What is an API?

**API (Application Programming Interface)** allows programs to communicate with each other.

### Key Concepts

- **Endpoint**: URL where the API can be accessed
- **Request**: Asking the API for data
- **Response**: Data returned by the API (usually JSON)
- **Parameters**: Options to customize your request

---

## IPO Framework for API Access

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  INPUT          │ --> │  PROCESS        │ --> │  OUTPUT         │
│                 │     │                 │     │                 │
│ - API endpoint  │     │ - HTTP request  │     │ - JSON data     │
│ - Parameters    │     │ - Parse JSON    │     │ - Analysis      │
│ - API key       │     │ - Extract data  │     │ - Visualization │
│                 │     │ - Analyze       │     │ - Report        │
└─────────────────┘     └─────────────────┘     └─────────────────┘
```

---

## Data Source: DATA.GOV.HK

Hong Kong's official open data portal provides:
- **2000+ datasets** across 20+ categories
- **Real-time data** (traffic, weather, transport)
- **Historical data** (demographics, economics)
- **Free public access** (no authentication required for most)

Website: [https://data.gov.hk](https://data.gov.hk)

---

## Example 1: MTR Next Train API

### API Information

- **Dataset**: Real-time MTR train arrival information
- **Endpoint**: `https://rt.data.gov.hk/v1/transport/mtr/getSchedule.php`
- **Documentation**: See `MTRexamples/Next_Train_API_Spec.pdf`

### Complete IPO Example

```python
import requests
import json

# ============================================
# INPUT: Define API parameters
# ============================================
endpoint = "https://rt.data.gov.hk/v1/transport/mtr/getSchedule.php"
params = {
    "line": "TML",    # Tuen Ma Line
    "sta": "TUM"      # Tuen Mun Station
}

# ============================================
# PROCESS: Fetch and parse data
# ============================================
# Step 1: Make HTTP request
response = requests.get(endpoint, params=params)

# Step 2: Parse JSON response
data = response.json()

# Step 3: Extract train information
if data['status'] == 1:  # Success
    train_data = data['data']
    platform_key = f"{params['line']}-{params['sta']}"
    
    # Get trains going DOWN (towards Wu Kai Sha)
    down_trains = train_data[platform_key]['DOWN']
    
    # ============================================
    # OUTPUT: Display results
    # ============================================
    print(f"=== Next Trains at {params['sta']} ({params['line']}) ===")
    print(f"Current Time: {data['curr_time']}")
    print(f"\nTrains to Wu Kai Sha (DOWN):")
    
    for train in down_trains:
        dest = train['dest']
        time = train['time']
        ttnt = train['ttnt']
        print(f"  - To {dest}: {time} ({ttnt} min)")
else:
    print(f"Error: {data['message']}")
```

---

## Example 2: Population Data Analysis

See `simpleDemo/download_population_data.py` for a complete example of:

```
INPUT: Census data API endpoint
  ↓
PROCESS: 
  - Fetch JSON data
  - Extract population statistics
  - Calculate growth rates
  - Compute demographic metrics
  ↓
OUTPUT:
  - CSV file with processed data
  - Statistical summary
  - Visualization charts
```

---

## Available Datasets on DATA.GOV.HK

### Transport
- MTR train schedules
- Bus arrival times
- Traffic speed maps
- Parking availability

### Environment
- Air quality indices
- Weather data
- Waste statistics

### Demographics
- Population by district
- Age distribution
- Employment statistics

### Health
- Hospital bed occupancy
- Disease surveillance
- Clinic wait times

---

## Quick Start Guide

### Step 1: Install Required Libraries

```bash
pip install requests pandas matplotlib
```

### Step 2: Run Simple Example

```bash
cd simpleDemo
python download_population_data.py
```

### Step 3: Explore MTR Example

```bash
cd MTRexamples
python mtr_api_test.py
```

---

## Hands-On Exercises

### Exercise 1: Explore Different Stations
Modify the MTR example to query:
- Central Station (CEN) on Island Line (ISL)
- Mongkok Station (MOK) on Tsuen Wan Line (TWL)
- Compare train frequencies

### Exercise 2: Data Analysis
Using the MTR API:
- Collect data from 5 different stations
- Calculate average wait times
- Identify busiest/quietest stations

### Exercise 3: Your Own Project
Choose a dataset from data.gov.hk and:
1. Read the API documentation
2. Write IPO-structured code
3. Fetch and analyze the data
4. Create a visualization

---

## Project Template

See `YourProject/` folder for:
- `sample_api_access.py` - Template for API requests
- `sample_analysis.py` - Template for data analysis
- `project_plan.md` - Project planning guide
- `requirements.txt` - Python dependencies

---

## Best Practices

### 1. Always Check API Status
```python
if response.status_code == 200:
    # Success
    data = response.json()
else:
    print(f"Error: {response.status_code}")
```

### 2. Handle Errors Gracefully
```python
try:
    response = requests.get(endpoint, params=params, timeout=10)
    data = response.json()
except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
```

### 3. Document Your IPO Steps
```python
# INPUT: Define what data you need
# PROCESS: Describe transformation steps
# OUTPUT: Specify expected results
```

### 4. Save Raw Data
```python
# Always save original API response
with open('raw_data.json', 'w') as f:
    json.dump(data, f, indent=2)
```

---

## Common MTR Line Codes

| Code | Line Name |
|------|-----------|
| `TML` | Tuen Ma Line |
| `ISL` | Island Line |
| `TWL` | Tsuen Wan Line |
| `KTL` | Kwun Tong Line |
| `EAL` | East Rail Line |
| `TKL` | Tseung Kwan O Line |
| `TCL` | Tung Chung Line |
| `AEL` | Airport Express |

See `README.md` in MTRexamples for complete station codes.

---

## Resources

### Documentation
- [DATA.GOV.HK Portal](https://data.gov.hk)
- [MTR API Specification](MTRexamples/Next_Train_API_Spec.pdf)
- [Python Requests Library](https://requests.readthedocs.io/)

### Datasets to Explore
1. **Real-time Transport**: Traffic, MTR, buses
2. **Environmental**: Air quality, weather
3. **Statistical**: Census, economics
4. **Healthcare**: Hospital data

---

## Assessment

Students will be evaluated on:
1. **API Integration** (30%): Successful data retrieval
2. **Data Analysis** (30%): Statistical insights
3. **Code Quality** (20%): IPO structure, documentation
4. **Visualization** (20%): Clear, informative charts

---

## Next Steps

After completing Module 2:
1. Move to **Module 3** (Web Crawler for NBA.com)
2. Apply API skills to LLM access in **Module 4**
3. Combine techniques for your final project

---

**Remember**: APIs are powerful tools for accessing real-world data. Think in IPO, code systematically, and document thoroughly!
