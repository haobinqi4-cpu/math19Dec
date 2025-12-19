# Module 1: Input-Process-Output Model

## Overview

This foundational module introduces MSc Math students to the fundamental **Input-Process-Output (IPO)** paradigm that underlies all computational and algorithmic thinking.

### Learning Objectives

By the end of this module, students will be able to:
1. Understand the IPO model as a conceptual framework
2. Apply IPO thinking to problem decomposition
3. Identify inputs, processes, and outputs in real-world scenarios
4. Design simple IPO-based solutions using Python

---

## What is the Input-Process-Output Model?

The IPO model is a fundamental pattern in:
- Computer Science
- Systems Thinking
- Data Analysis
- Algorithm Design

```
┌─────────┐     ┌─────────┐     ┌─────────┐
│  INPUT  │ --> │ PROCESS │ --> │ OUTPUT  │
└─────────┘     └─────────┘     └─────────┘
```

### Components

1. **INPUT**: Data or information received
   - User input
   - File data
   - API responses
   - Sensor readings

2. **PROCESS**: Transformation or computation
   - Calculations
   - Data cleaning
   - Analysis
   - Algorithm execution

3. **OUTPUT**: Results produced
   - Printed results
   - Files written
   - Visualizations
   - API responses

---

## Example 1: Simple Mathematical Function

```python
# INPUT: Two numbers
a = 5
b = 3

# PROCESS: Add the numbers
result = a + b

# OUTPUT: Display the result
print(f"The sum is: {result}")
```

**IPO Breakdown:**
- **Input**: `a=5`, `b=3`
- **Process**: Addition operation
- **Output**: `The sum is: 8`

---

## Example 2: Data Analysis Pipeline

```python
import pandas as pd

# INPUT: Load data from CSV
data = pd.read_csv('population_data.csv')

# PROCESS: Calculate average population
average_pop = data['population'].mean()

# PROCESS: Find maximum population
max_pop = data['population'].max()

# OUTPUT: Display results
print(f"Average Population: {average_pop:,.0f}")
print(f"Maximum Population: {max_pop:,.0f}")
```

**IPO Breakdown:**
- **Input**: CSV file with population data
- **Process**: Statistical calculations (mean, max)
- **Output**: Formatted statistical results

---

## Example 3: API Data Pipeline

```python
import requests

# INPUT: Fetch data from API
response = requests.get('https://api.example.com/data')
json_data = response.json()

# PROCESS: Extract specific field
values = [item['value'] for item in json_data['results']]

# PROCESS: Calculate sum
total = sum(values)

# OUTPUT: Save to file
with open('output.txt', 'w') as f:
    f.write(f"Total: {total}\n")
```

**IPO Breakdown:**
- **Input**: API response (JSON)
- **Process**: Data extraction and aggregation
- **Output**: Text file with results

---

## Exercises

### Exercise 1: Temperature Converter
Design an IPO solution that:
- **Input**: Temperature in Celsius
- **Process**: Convert to Fahrenheit using formula `F = (C × 9/5) + 32`
- **Output**: Display both temperatures

### Exercise 2: Grade Calculator
Design an IPO solution that:
- **Input**: List of student scores
- **Process**: Calculate average, find highest and lowest scores
- **Output**: Summary statistics

### Exercise 3: Text Analysis
Design an IPO solution that:
- **Input**: Read a text file
- **Process**: Count words, characters, and lines
- **Output**: Display statistics

---

## Application to Modules 2-4

Understanding IPO helps you approach complex problems:

### Module 2 (Data.gov.hk API)
- **Input**: API request parameters
- **Process**: Fetch, parse, analyze data
- **Output**: Visualizations, reports

### Module 3 (NBA Web Crawler)
- **Input**: NBA website URLs
- **Process**: Crawl, extract, clean data
- **Output**: Structured dataset

### Module 4 (LLM API)
- **Input**: User prompt/query
- **Process**: LLM processing
- **Output**: Generated text/analysis

---

## Key Takeaways

1. **Every computational task follows IPO**
2. **Clear separation** makes debugging easier
3. **IPO thinking** aids problem decomposition
4. **Documentation** of each stage improves clarity

---

## Next Steps

After mastering IPO concepts:
1. Move to **Module 2** for API data access
2. Apply IPO thinking to real-world problems
3. Use IPO as a framework for all your projects

---

**Remember**: Good programmers think in IPO before writing code!

