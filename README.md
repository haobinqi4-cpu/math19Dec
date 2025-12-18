# Math AI Workshop - MSc Mathematics Students

## Overview

Welcome to the Math AI Workshop! This course teaches MSc Mathematics students how to leverage AI tools, APIs, and data analysis techniques for modern computational mathematics and data science.

---

## Course Structure

The workshop consists of 4 progressive modules:

### Module 1: Input-Process-Output Model
**Foundational Concepts**
- Learn the IPO paradigm for computational thinking
- Apply IPO to problem decomposition
- Master systematic algorithm design

📁 **Folder**: `Module1_InputProcessOutput/`

---

### Module 2: Data.gov.hk API Access & Analysis
**Government Open Data**
- Access Hong Kong government data via APIs
- Parse JSON responses and extract data
- Perform statistical analysis with Python
- Create data visualizations

📁 **Folder**: `Module2_DataGovAPI/`

**Key Example**: MTR Next Train API real-time data access

---

### Module 3: Web Crawler for NBA.com
**Ethical Web Scraping**
- Understand robots.txt and web crawling ethics
- Build Python web crawlers
- Extract structured data from HTML
- Analyze sports statistics programmatically

📁 **Folder**: `Module3_WebCrawler_NBA/`

**Key Skills**: Beautiful Soup, requests, sitemap parsing, rate limiting

---

### Module 4: LLM API Programming
**AI Integration**
- Access HKBU Gen AI services via API
- Send prompts and process LLM responses
- Integrate AI into data analysis workflows
- Build intelligent applications

📁 **Folder**: `Module4_LLM_API/`

**Platform**: HKBU Generative AI Services

---

## Learning Progression

```
Module 1: IPO Model (Foundation)
    ↓
Module 2: API Data Access (Apply IPO to APIs)
    ↓
Module 3: Web Crawling (Apply IPO to scraping)
    ↓
Module 4: LLM Integration (Combine all skills)
    ↓
Final Project: Integrated Application
```

---

## Quick Start Guide

### Prerequisites

**Required Software**:
- Python 3.8 or higher
- pip package manager
- Text editor or IDE (VS Code, PyCharm recommended)

**Required Python Libraries**:
```bash
pip install requests pandas matplotlib beautifulsoup4 lxml python-dotenv
```

---

### Getting Started

#### 1. Clone or Download Materials
```bash
cd /path/to/mathAIworkshop
```

#### 2. Start with Module 1
```bash
cd Module1_InputProcessOutput
python exercises.py
```

#### 3. Progress Through Modules Sequentially
Each module builds on previous concepts

#### 4. Complete Module Exercises
Every module includes hands-on exercises

---

## Module Details

### Module 1: Input-Process-Output
**Duration**: 1-2 hours  
**Prerequisites**: Basic Python knowledge  
**Deliverables**: Exercise solutions

**Learning Outcomes**:
- ✅ Understand IPO model
- ✅ Apply to problem-solving
- ✅ Design structured solutions

**Files**:
- `README.md` - Concepts and examples
- `exercises.py` - Hands-on exercises

---

### Module 2: Data.gov.hk API
**Duration**: 3-4 hours  
**Prerequisites**: Module 1  
**Deliverables**: API data analysis project

**Learning Outcomes**:
- ✅ Understand REST APIs
- ✅ Access government data
- ✅ Parse JSON responses
- ✅ Perform statistical analysis

**Key Files**:
- `README.md` - API documentation
- `MTRexamples/` - Working MTR API examples
- `simpleDemo/` - Population data demo
- `YourProject/` - Student project template

---

### Module 3: NBA Web Crawler
**Duration**: 4-5 hours  
**Prerequisites**: Modules 1-2  
**Deliverables**: Web crawler + analysis report

**Learning Outcomes**:
- ✅ Understand web scraping ethics
- ✅ Parse robots.txt and sitemaps
- ✅ Extract structured HTML data
- ✅ Implement rate limiting

**Key Files**:
- `README.md` - Crawling guide
- `nba_crawler.py` - Main crawler implementation
- `requirements.txt` - Dependencies

---

### Module 4: LLM API Programming
**Duration**: 3-4 hours  
**Prerequisites**: Modules 1-3  
**Deliverables**: LLM-integrated application

**Learning Outcomes**:
- ✅ Access HKBU Gen AI API
- ✅ Send prompts programmatically
- ✅ Process LLM responses
- ✅ Integrate AI into workflows

**Key Files**:
- `README.md` - API documentation
- `llm_client.py` - Reusable LLM client
- `requirements.txt` - Dependencies

---

## Final Project Ideas

Combine all 4 modules for your final project:

### Project 1: Smart Government Data Analyst
- **Module 2**: Fetch data from data.gov.hk API
- **Module 4**: Use LLM to analyze and generate insights
- **Output**: Automated policy analysis report

### Project 2: Sports Analytics Platform
- **Module 3**: Crawl NBA.com for player statistics
- **Module 2**: Integrate with sports APIs
- **Module 4**: Generate AI-powered game predictions
- **Output**: Interactive sports analysis dashboard

### Project 3: Research Assistant Bot
- **Module 3**: Crawl academic resources
- **Module 2**: Access research databases via API
- **Module 4**: Summarize papers with LLM
- **Output**: Automated literature review tool

### Project 4: Data-Driven News Monitor
- **Module 3**: Crawl news websites
- **Module 2**: Fetch economic indicators via API
- **Module 4**: Generate trend analysis reports
- **Output**: Automated news digest

---

## Assessment

### Individual Module Assessments (60%)
- Module 1: Exercises (10%)
- Module 2: API Project (20%)
- Module 3: Web Crawler (15%)
- Module 4: LLM Integration (15%)

### Final Project (40%)
- Project proposal (5%)
- Implementation (25%)
- Documentation (5%)
- Presentation (5%)

---

## Grading Rubric

### Code Quality (30%)
- ✅ Proper IPO structure
- ✅ Clear comments and documentation
- ✅ Error handling
- ✅ Code organization

### Functionality (30%)
- ✅ Meets requirements
- ✅ Produces correct output
- ✅ Handles edge cases
- ✅ Efficient implementation

### Analysis & Insights (20%)
- ✅ Statistical rigor
- ✅ Meaningful conclusions
- ✅ Data visualization
- ✅ Critical thinking

### Ethics & Best Practices (20%)
- ✅ Respect robots.txt
- ✅ Rate limiting
- ✅ API key security
- ✅ Data privacy

---

## Important Ethical Guidelines

### API Access
- ✅ Use rate limiting (minimum 1-2 seconds between requests)
- ✅ Use descriptive User-Agent strings
- ✅ Respect API terms of service
- ❌ Never share API keys publicly
- ❌ Don't overload servers

### Web Crawling
- ✅ Always check robots.txt first
- ✅ Implement polite crawling practices
- ✅ Cache data to avoid re-crawling
- ❌ Never ignore Disallow directives
- ❌ Don't collect personal data

### LLM Usage
- ✅ Store API keys in environment variables
- ✅ Handle sensitive data appropriately
- ✅ Use AI responsibly and ethically
- ❌ Never commit API keys to Git
- ❌ Don't rely solely on LLM output

---

## Resources

### Python Libraries Documentation
- [Requests](https://docs.python-requests.org/) - HTTP library
- [Pandas](https://pandas.pydata.org/docs/) - Data analysis
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Web scraping
- [Matplotlib](https://matplotlib.org/) - Visualization

### Data Sources
- [DATA.GOV.HK](https://data.gov.hk) - Hong Kong open data
- [NBA.com](https://www.nba.com) - Basketball statistics
- [HKBU Gen AI](https://genai.hkbu.edu.hk) - LLM services

### Best Practices
- [Web Scraping Ethics](https://towardsdatascience.com/ethics-in-web-scraping-b96b18136f01)
- [API Best Practices](https://swagger.io/resources/articles/best-practices-in-api-design/)
- [Python Style Guide (PEP 8)](https://pep8.org/)

---

## Technical Support

### Common Issues

**Issue**: `ModuleNotFoundError: No module named 'requests'`
**Solution**: `pip install requests`

**Issue**: `403 Forbidden` error when crawling
**Solution**: Check robots.txt, add proper User-Agent

**Issue**: API key not found
**Solution**: Set environment variable `export HKBU_GENAI_API_KEY="..."`

**Issue**: Rate limit exceeded
**Solution**: Add `time.sleep(2)` between requests

---

## Schedule Recommendation

### Week 1: Foundation
- **Days 1-2**: Module 1 (IPO Model)
- **Days 3-5**: Module 2 (API Access)

### Week 2: Advanced Topics
- **Days 1-3**: Module 3 (Web Crawling)
- **Days 4-5**: Module 4 (LLM API)

### Week 3: Integration
- **Days 1-3**: Final project implementation
- **Days 4-5**: Documentation and presentation

---

## Office Hours & Support

- **Instructor**: [Contact Information]
- **Office Hours**: [Time and Location]
- **Email**: [Email Address]
- **Discussion Forum**: [Link if applicable]

---

## Academic Integrity

- All code must be your own work
- Properly cite any external code or resources
- LLM-assisted code must be understood and documented
- Collaboration is encouraged, but submissions must be individual

---

## Getting Help

### For Technical Issues:
1. Check module README files
2. Review error messages carefully
3. Search Python documentation
4. Ask in discussion forum
5. Attend office hours

### For Conceptual Questions:
1. Re-read module materials
2. Work through examples
3. Discuss with classmates
4. Consult instructor

---

## Success Tips

1. **Start Early** - Don't wait until deadlines
2. **Test Frequently** - Run code often, catch errors early
3. **Document Everything** - Comments save time later
4. **Think in IPO** - Always structure code this way
5. **Be Ethical** - Follow all guidelines strictly
6. **Ask Questions** - No question is too small
7. **Experiment** - Try different approaches
8. **Have Fun** - Enjoy learning!

---

## Next Steps

1. ✅ Read this README completely
2. ✅ Set up Python environment
3. ✅ Install required libraries
4. ✅ Start Module 1
5. ✅ Complete exercises sequentially
6. ✅ Begin planning final project

---

## Course Objectives

By the end of this workshop, you will be able to:

1. **Apply IPO thinking** to computational problems
2. **Access and analyze** real-world data via APIs
3. **Build ethical web crawlers** for data collection
4. **Integrate LLM capabilities** into Python programs
5. **Combine multiple techniques** for complex projects
6. **Follow best practices** for code quality and ethics
7. **Create professional** data analysis applications

---

## Contact Information

For questions about this workshop:
- Review module README files first
- Check technical support section above
- Contact instructor during office hours
- Post in course discussion forum

---

**Welcome to Math AI Workshop! Let's build intelligent data applications together! 🚀**

---

*Last Updated: December 2025*  
*For MSc Mathematics Students*

