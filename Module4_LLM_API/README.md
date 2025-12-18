# Module 4: LLM API Programming with HKBU Gen AI Services

## Overview

This module teaches MSc Mathematics students how to programmatically access Large Language Models (LLMs) through APIs, specifically using HKBU's Gen AI services. Students will learn to integrate AI capabilities into their Python programs using the Input-Process-Output model.

### Learning Objectives

By the end of this module, students will be able to:
1. Understand LLM API concepts and authentication
2. Access HKBU Gen AI services programmatically
3. Send prompts and process LLM responses
4. Integrate LLM capabilities into data analysis workflows
5. Apply IPO model to AI-assisted programming
6. Build intelligent applications combining APIs and LLMs

---

## IPO Framework for LLM API Access

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  INPUT          │ --> │  PROCESS        │ --> │  OUTPUT         │
│                 │     │                 │     │                 │
│ - User prompt   │     │ - API request   │     │ - LLM response  │
│ - API key       │     │ - LLM processing│     │ - Parsed text   │
│ - Parameters    │     │ - Response parse│     │ - Analysis      │
│ - Context       │     │ - Error handling│     │ - Actions       │
└─────────────────┘     └─────────────────┘     └─────────────────┘
```

---

## What is an LLM API?

**LLM (Large Language Model) API** allows programs to:
- Send text prompts to AI models
- Receive intelligent responses
- Automate tasks requiring language understanding
- Integrate AI into applications

### Key Concepts

- **Endpoint**: API URL for LLM service
- **API Key**: Authentication credential
- **Prompt**: Input text/question sent to LLM
- **Response**: AI-generated output
- **Parameters**: Settings like temperature, max tokens

---

## HKBU Gen AI Services

### Access Information

- **Service**: HKBU Generative AI Platform
- **Available Models**: GPT-4, Claude, Gemini, etc.
- **Authentication**: API key from HKBU portal
- **Documentation**: [HKBU Gen AI Portal](https://genai.hkbu.edu.hk)

### Getting Your API Key

1. Visit HKBU Gen AI portal
2. Login with HKBU credentials
3. Navigate to API section
4. Generate/copy your API key
5. Store securely (never commit to Git!)

---

## Example 1: Basic LLM API Call

### Using OpenAI-Compatible API

```python
import requests
import json
import os

# ===== INPUT =====
# API Configuration
API_ENDPOINT = "https://genai.hkbu.edu.hk/v1/chat/completions"
API_KEY = os.getenv("HKBU_GENAI_API_KEY")  # Store in environment variable

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# User prompt
prompt = "Explain the Central Limit Theorem in simple terms."

# Request payload
payload = {
    "model": "gpt-4",
    "messages": [
        {"role": "user", "content": prompt}
    ],
    "temperature": 0.7,
    "max_tokens": 500
}

# ===== PROCESS =====
response = requests.post(API_ENDPOINT, headers=headers, json=payload)

if response.status_code == 200:
    data = response.json()
    
    # ===== OUTPUT =====
    llm_response = data['choices'][0]['message']['content']
    print("LLM Response:")
    print("-" * 60)
    print(llm_response)
    print("-" * 60)
else:
    print(f"Error: {response.status_code}")
    print(response.text)
```

---

## Example 2: LLM-Assisted Data Analysis

### Analyze Data and Ask LLM for Insights

```python
import pandas as pd
import requests
import json

class LLMDataAnalyst:
    """
    Combine data analysis with LLM insights
    """
    
    def __init__(self, api_key):
        self.api_key = api_key
        self.endpoint = "https://genai.hkbu.edu.hk/v1/chat/completions"
    
    def ask_llm(self, prompt, model="gpt-4"):
        """
        INPUT: Question/prompt
        PROCESS: Send to LLM API
        OUTPUT: LLM response
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7
        }
        
        response = requests.post(self.endpoint, headers=headers, json=payload)
        
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content']
        else:
            return f"Error: {response.status_code}"
    
    def analyze_dataset(self, df):
        """
        Analyze DataFrame and get LLM insights
        
        INPUT: Pandas DataFrame
        PROCESS: Calculate stats + ask LLM for interpretation
        OUTPUT: Combined analysis
        """
        # ===== INPUT =====
        print("Dataset shape:", df.shape)
        
        # ===== PROCESS =====
        # Step 1: Basic statistics
        stats_summary = df.describe().to_string()
        
        # Step 2: Create prompt for LLM
        prompt = f"""
I have a dataset with the following statistical summary:

{stats_summary}

Please provide:
1. Key insights from this data
2. Potential patterns or anomalies
3. Suggested next steps for analysis
"""
        
        # Step 3: Get LLM insights
        llm_insights = self.ask_llm(prompt)
        
        # ===== OUTPUT =====
        return {
            'statistics': stats_summary,
            'llm_insights': llm_insights
        }


# USAGE EXAMPLE
if __name__ == "__main__":
    # Load data
    data = {
        'scores': [85, 92, 78, 90, 88, 76, 95, 89],
        'study_hours': [5, 8, 4, 7, 6, 3, 9, 7]
    }
    df = pd.DataFrame(data)
    
    # Initialize analyst
    analyst = LLMDataAnalyst(api_key=os.getenv("HKBU_GENAI_API_KEY"))
    
    # Get analysis
    result = analyst.analyze_dataset(df)
    
    print("\n=== Statistical Summary ===")
    print(result['statistics'])
    
    print("\n=== LLM Insights ===")
    print(result['llm_insights'])
```

---

## Example 3: Automated Code Generation

### Use LLM to Generate Analysis Code

```python
def generate_analysis_code(data_description, analysis_goal):
    """
    INPUT: Description of data and analysis goal
    PROCESS: Ask LLM to generate Python code
    OUTPUT: Executable Python code
    """
    prompt = f"""
Generate Python code using pandas to analyze the following data:

Data Description: {data_description}
Analysis Goal: {analysis_goal}

Please provide complete, executable code with comments.
"""
    
    # Send to LLM API
    llm_response = ask_llm(prompt)
    
    return llm_response


# Example usage
data_desc = "A CSV with columns: date, temperature, humidity"
goal = "Calculate monthly average temperature and plot trends"

code = generate_analysis_code(data_desc, goal)
print("Generated Code:")
print(code)
```

---

## Example 4: Combining Modules 2, 3, 4

### Complete Pipeline: API Data → Web Crawl → LLM Analysis

```python
import requests
import pandas as pd
from llm_api import LLMDataAnalyst

# ===== MODULE 2: Get data from API =====
# Fetch population data from data.gov.hk
api_response = requests.get("https://api.data.gov.hk/v1/...")
population_data = api_response.json()

# ===== MODULE 3: Web crawling for context =====
# Crawl related news or reports (if allowed by robots.txt)
# ... crawler code ...

# ===== MODULE 4: LLM analysis =====
# Convert to DataFrame
df = pd.DataFrame(population_data)

# Ask LLM for insights
analyst = LLMDataAnalyst(api_key=API_KEY)
insights = analyst.analyze_dataset(df)

# Generate report
prompt = f"""
Based on this population data analysis:

{insights['statistics']}

Write a 200-word executive summary for policymakers.
"""

summary = analyst.ask_llm(prompt)
print(summary)
```

---

## Security Best Practices

### ✅ DO

1. **Store API keys in environment variables**
   ```python
   import os
   API_KEY = os.getenv("HKBU_GENAI_API_KEY")
   ```

2. **Never commit API keys to Git**
   Add to `.gitignore`:
   ```
   .env
   config.py
   *_api_key.txt
   ```

3. **Use `.env` files for local development**
   ```bash
   # .env file
   HKBU_GENAI_API_KEY=your_key_here
   ```
   
   ```python
   # Load in Python
   from dotenv import load_dotenv
   load_dotenv()
   ```

4. **Handle errors gracefully**
   ```python
   try:
       response = requests.post(...)
   except requests.exceptions.RequestException as e:
       print(f"API Error: {e}")
   ```

### ❌ DON'T

1. Hardcode API keys in code
2. Share API keys publicly
3. Commit `.env` files
4. Ignore rate limits
5. Store keys in plain text files tracked by Git

---

## Common Use Cases

### 1. Data Interpretation
```python
# Get LLM to explain statistical results
prompt = f"Explain what a p-value of {p_val} means in this context"
explanation = ask_llm(prompt)
```

### 2. Code Debugging
```python
# Ask LLM to help debug code
prompt = f"""
I'm getting this error:
{error_message}

In this code:
{code_snippet}

What's wrong and how do I fix it?
"""
debug_help = ask_llm(prompt)
```

### 3. Report Generation
```python
# Generate professional reports
prompt = f"""
Write a technical report about:
{analysis_results}

Include: introduction, methodology, findings, conclusion
"""
report = ask_llm(prompt)
```

### 4. Data Cleaning Suggestions
```python
# Ask for data cleaning advice
prompt = f"""
I have missing values in these columns:
{missing_data_summary}

What are best practices for handling this?
"""
advice = ask_llm(prompt)
```

---

## API Parameters Explained

### Common Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| `model` | LLM model to use | `"gpt-4"`, `"claude-3"` |
| `temperature` | Creativity (0-1) | `0.7` (balanced) |
| `max_tokens` | Response length limit | `500` |
| `top_p` | Nucleus sampling | `0.9` |
| `frequency_penalty` | Reduce repetition | `0.5` |

### Temperature Guide

- **0.0-0.3**: Factual, deterministic (for math, code)
- **0.4-0.7**: Balanced (general purpose)
- **0.8-1.0**: Creative (for writing, brainstorming)

---

## Exercises

### Exercise 1: Basic API Integration
Write code to:
1. Load API key from environment variable
2. Send a math question to LLM
3. Parse and display the response

### Exercise 2: Data Analysis Assistant
Create a program that:
1. Loads a CSV file
2. Calculates basic statistics
3. Asks LLM to interpret the results
4. Saves the analysis to a file

### Exercise 3: Automated Report Generator
Build a tool that:
1. Takes analysis results as input
2. Uses LLM to generate executive summary
3. Formats as markdown document
4. Saves to file

### Exercise 4: Multi-Module Integration
Combine all modules:
1. Fetch data from data.gov.hk (Module 2)
2. Optionally crawl related web data (Module 3)
3. Use LLM to analyze and generate insights (Module 4)
4. Create final report with visualizations

---

## Project Structure

```
Module4_LLM_API/
├── README.md              # This file
├── requirements.txt       # Python dependencies
├── .env.example          # Example environment variables
├── examples/
│   ├── basic_llm.py      # Simple LLM call
│   ├── data_analysis.py  # LLM + data analysis
│   └── report_gen.py     # Automated reports
├── utils/
│   ├── llm_client.py     # Reusable LLM client
│   └── security.py       # API key management
└── projects/
    ├── YOUR_PROJECT/     # Student project template
    └── sample_project/   # Example project
```

---

## Installation

```bash
pip install requests pandas python-dotenv openai
```

Or use requirements.txt:

```bash
pip install -r requirements.txt
```

---

## Quick Start

```bash
# 1. Set up API key
export HKBU_GENAI_API_KEY="your_key_here"

# 2. Run basic example
python examples/basic_llm.py

# 3. Try data analysis example
python examples/data_analysis.py

# 4. Generate automated report
python examples/report_gen.py
```

---

## Assessment

Students will be evaluated on:
1. **API Integration** (25%): Proper authentication, error handling
2. **Code Quality** (25%): IPO structure, security practices
3. **Application** (25%): Creative use of LLM capabilities
4. **Integration** (25%): Combining with Modules 1-3

---

## Resources

### Documentation
- [HKBU Gen AI Portal](https://genai.hkbu.edu.hk)
- [OpenAI API Reference](https://platform.openai.com/docs/api-reference)
- [Python Requests](https://docs.python-requests.org/)
- [Python dotenv](https://pypi.org/project/python-dotenv/)

### Tutorials
- [LLM API Best Practices](https://platform.openai.com/docs/guides/production-best-practices)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)

---

## Final Project Ideas

1. **Smart Data Explorer**: Combine API data + LLM analysis
2. **Automated Research Assistant**: Web crawl + LLM summarization
3. **Policy Analysis Tool**: Government data + LLM insights
4. **Interactive Q&A System**: Data-driven chatbot

---

## Next Steps

After completing Module 4:
1. **Final Project**: Integrate all 4 modules
2. **Explore advanced topics**: Streaming, function calling, embeddings
3. **Build portfolio**: Create showcase projects

---

**Remember**: LLMs are powerful tools. Use them ethically, securely, and creatively!

