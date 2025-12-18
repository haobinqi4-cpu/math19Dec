# Module 3: Web Crawler for NBA.com

## Overview

This module teaches MSc Mathematics students how to ethically crawl sports data from NBA.com using Python. Students will learn to respect robots.txt, parse sitemaps, extract structured data, and apply statistical analysis to basketball statistics.

### Learning Objectives

By the end of this module, students will be able to:
1. Understand web crawling ethics and robots.txt
2. Implement ethical web scrapers using Python
3. Extract structured data from HTML
4. Parse XML sitemaps for efficient crawling
5. Apply IPO model to web data collection
6. Analyze sports statistics programmatically

---

## IPO Framework for Web Crawling

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  INPUT          │ --> │  PROCESS        │ --> │  OUTPUT         │
│                 │     │                 │     │                 │
│ - Target URL    │     │ - Check robots  │     │ - HTML content  │
│ - robots.txt    │     │ - HTTP request  │     │ - Extracted data│
│ - Sitemap       │     │ - Parse HTML    │     │ - CSV/JSON files│
│                 │     │ - Extract data  │     │ - Statistics    │
│                 │     │ - Rate limiting │     │ - Visualizations│
└─────────────────┘     └─────────────────┘     └─────────────────┘
```

---

## Why NBA.com?

**NBA.com** is an excellent learning resource because:
- ✅ Rich statistical data (player stats, team standings)
- ✅ Well-structured HTML
- ✅ Public robots.txt available
- ✅ Sitemaps for navigation
- ✅ Real-world sports analytics use case

**Website**: [https://www.nba.com](https://www.nba.com)  
**Robots.txt**: [https://www.nba.com/robots.txt](https://www.nba.com/robots.txt)

---

## Step 1: Understanding robots.txt

### What is robots.txt?

A file that tells web crawlers which parts of a website can be accessed.

### Check NBA.com robots.txt

```python
import requests

# INPUT: robots.txt URL
url = "https://www.nba.com/robots.txt"

# PROCESS: Fetch robots.txt
response = requests.get(url)

# OUTPUT: Display rules
print(response.text)
```

### Key Rules to Respect

```
User-agent: *
Disallow: /admin/
Disallow: /private/
Allow: /stats/
Allow: /players/
```

**Important**: Always respect `Disallow` directives!

---

## Step 2: Finding Sitemaps

Sitemaps list all pages on a website, making crawling more efficient.

### Common Sitemap Locations

```python
sitemap_urls = [
    "https://www.nba.com/sitemap.xml",
    "https://www.nba.com/sitemap_index.xml",
    "https://www.nba.com/sitemap-players.xml",
    "https://www.nba.com/sitemap-teams.xml"
]

# Try each URL
for url in sitemap_urls:
    response = requests.get(url)
    if response.status_code == 200:
        print(f"✓ Found: {url}")
    else:
        print(f"✗ Not found: {url}")
```

---

## Step 3: Basic Web Crawler

### Simple NBA Stats Crawler

```python
import requests
from bs4 import BeautifulSoup
import time
import json

class NBAStatsCrawler:
    """
    Ethical web crawler for NBA.com statistics
    Implements IPO model with rate limiting
    """
    
    def __init__(self):
        self.base_url = "https://www.nba.com"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Educational-Crawler-MSc-Math-HKBU/1.0'
        })
        
    def check_robots_txt(self):
        """INPUT: Fetch robots.txt"""
        url = f"{self.base_url}/robots.txt"
        response = self.session.get(url)
        return response.text
    
    def crawl_page(self, url):
        """
        IPO: Crawl a single page
        
        INPUT: URL to crawl
        PROCESS: Fetch HTML, extract data
        OUTPUT: Structured data
        """
        # INPUT
        print(f"Crawling: {url}")
        
        # PROCESS: Fetch page
        response = self.session.get(url)
        
        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            return None
        
        # PROCESS: Parse HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # PROCESS: Extract data (example: find all tables)
        tables = soup.find_all('table')
        
        # OUTPUT
        data = {
            'url': url,
            'title': soup.title.string if soup.title else '',
            'num_tables': len(tables),
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
        }
        
        # Rate limiting (IMPORTANT!)
        time.sleep(2)  # Wait 2 seconds between requests
        
        return data
    
    def crawl_multiple(self, urls, output_file='nba_data.json'):
        """
        Crawl multiple pages and save results
        """
        results = []
        
        for url in urls:
            data = self.crawl_page(url)
            if data:
                results.append(data)
        
        # OUTPUT: Save to file
        with open(output_file, 'w') as f:
            json.dump(results, f, indent=2)
        
        print(f"Saved {len(results)} pages to {output_file}")
        return results


# USAGE EXAMPLE
if __name__ == "__main__":
    crawler = NBAStatsCrawler()
    
    # Example URLs (adjust based on actual site structure)
    urls = [
        "https://www.nba.com/stats/players",
        "https://www.nba.com/stats/teams"
    ]
    
    results = crawler.crawl_multiple(urls)
    print(f"Crawled {len(results)} pages")
```

---

## Step 4: Extract Player Statistics

### Example: Parse Player Stats Table

```python
def extract_player_stats(html_content):
    """
    INPUT: HTML content with player stats
    PROCESS: Parse table and extract data
    OUTPUT: List of player dictionaries
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find stats table (selector may need adjustment)
    table = soup.find('table', {'class': 'stats-table'})
    
    if not table:
        return []
    
    players = []
    rows = table.find_all('tr')[1:]  # Skip header
    
    for row in rows:
        cols = row.find_all('td')
        if len(cols) >= 5:
            player = {
                'name': cols[0].text.strip(),
                'team': cols[1].text.strip(),
                'points': float(cols[2].text.strip()),
                'rebounds': float(cols[3].text.strip()),
                'assists': float(cols[4].text.strip())
            }
            players.append(player)
    
    return players
```

---

## Step 5: Data Analysis

### Statistical Analysis of Player Data

```python
import pandas as pd
import matplotlib.pyplot as plt

def analyze_player_stats(players):
    """
    INPUT: List of player dictionaries
    PROCESS: Statistical analysis
    OUTPUT: Summary statistics and visualizations
    """
    # Convert to DataFrame
    df = pd.DataFrame(players)
    
    # PROCESS: Calculate statistics
    stats = {
        'avg_points': df['points'].mean(),
        'avg_rebounds': df['rebounds'].mean(),
        'avg_assists': df['assists'].mean(),
        'top_scorer': df.loc[df['points'].idxmax(), 'name'],
        'max_points': df['points'].max()
    }
    
    # OUTPUT: Print statistics
    print("=== Player Statistics Summary ===")
    print(f"Average Points: {stats['avg_points']:.2f}")
    print(f"Average Rebounds: {stats['avg_rebounds']:.2f}")
    print(f"Average Assists: {stats['avg_assists']:.2f}")
    print(f"Top Scorer: {stats['top_scorer']} ({stats['max_points']} pts)")
    
    # OUTPUT: Visualization
    df.plot(x='name', y=['points', 'rebounds', 'assists'], 
            kind='bar', figsize=(12, 6))
    plt.title('Player Statistics Comparison')
    plt.xlabel('Player')
    plt.ylabel('Stats')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('player_stats.png')
    
    return stats
```

---

## Ethical Guidelines

### ✅ DO

1. **Check robots.txt first**
2. **Use rate limiting** (minimum 1-2 seconds between requests)
3. **Identify yourself** (descriptive User-Agent)
4. **Respect Disallow rules**
5. **Handle errors gracefully**
6. **Cache data** (don't re-crawl unnecessarily)

### ❌ DON'T

1. **Ignore robots.txt**
2. **Overload servers** (no rapid-fire requests)
3. **Crawl private/disallowed areas**
4. **Disguise your crawler**
5. **Collect personal data**
6. **Use data unethically**

---

## Project Structure

```
Module3_WebCrawler_NBA/
├── README.md                  # This file
├── requirements.txt           # Python dependencies
├── nba_crawler.py            # Main crawler script
├── analyze_nba_data.py       # Analysis script
├── examples/
│   ├── basic_crawler.py      # Simple example
│   ├── sitemap_parser.py     # Sitemap parsing
│   └── stats_extractor.py    # Data extraction
├── data/
│   ├── raw/                  # Raw HTML pages
│   ├── processed/            # Extracted data (JSON/CSV)
│   └── analysis/             # Analysis results
└── docs/
    ├── ETHICS.md             # Ethical guidelines
    └── TUTORIAL.md           # Step-by-step tutorial
```

---

## Exercises

### Exercise 1: Check robots.txt
Write code to:
1. Fetch NBA.com robots.txt
2. Parse the rules
3. Determine which paths are allowed/disallowed

### Exercise 2: Find Sitemaps
Write code to:
1. Discover all sitemaps on NBA.com
2. Parse the XML
3. List all player or team pages

### Exercise 3: Extract Team Stats
Create a crawler that:
1. Visits team stats page
2. Extracts standings table
3. Calculates win percentages
4. Identifies top 5 teams

### Exercise 4: Player Comparison
Build a tool that:
1. Crawls data for 5 players
2. Compares their statistics
3. Creates visualizations
4. Generates a summary report

---

## Installation

```bash
pip install requests beautifulsoup4 lxml pandas matplotlib
```

Or use requirements.txt:

```bash
pip install -r requirements.txt
```

---

## Quick Start

```bash
# 1. Check robots.txt
python examples/basic_crawler.py --check-robots

# 2. Find sitemaps
python examples/sitemap_parser.py

# 3. Crawl sample pages
python nba_crawler.py --max-pages 5

# 4. Analyze data
python analyze_nba_data.py
```

---

## Assessment

Students will be evaluated on:
1. **Ethics Compliance** (25%): Proper robots.txt handling, rate limiting
2. **Code Quality** (25%): Clean IPO structure, error handling
3. **Data Extraction** (25%): Accurate parsing, data quality
4. **Analysis** (25%): Statistical insights, visualizations

---

## Resources

### Documentation
- [robots.txt Specification](https://www.robotstxt.org/)
- [Beautiful Soup Docs](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests Library](https://docs.python-requests.org/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)

### Tutorials
- [Web Scraping Ethics](https://towardsdatascience.com/ethics-in-web-scraping-b96b18136f01)
- [Python Web Scraping](https://realpython.com/python-web-scraping-practical-introduction/)

---

## Next Steps

After completing Module 3:
1. Move to **Module 4** (LLM API Programming)
2. Combine crawling + analysis for final project
3. Explore advanced topics (async crawling, data pipelines)

---

**Remember**: Ethical crawling is responsible crawling. Always respect website policies and resource limits!

