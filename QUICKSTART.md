# Quick Start Guide - Math AI Workshop

## ⚡ Get Started in 5 Minutes

### Step 1: Install Python Libraries (2 minutes)

```bash
pip install requests pandas matplotlib beautifulsoup4 lxml python-dotenv
```

### Step 2: Verify Installation (1 minute)

```bash
python -c "import requests, pandas, matplotlib; print('✓ All libraries installed!')"
```

### Step 3: Start Module 1 (2 minutes)

```bash
cd Module1_InputProcessOutput
python exercises.py
```

---

## 📚 Module Overview

| Module | Topic | Duration | Key Skills |
|--------|-------|----------|------------|
| 1 | IPO Model | 1-2 hours | Computational thinking |
| 2 | Data.gov.hk API | 3-4 hours | API access, JSON parsing |
| 3 | NBA Web Crawler | 4-5 hours | Web scraping, ethics |
| 4 | LLM API | 3-4 hours | AI integration |

---

## 🎯 What to Do First

### Complete Beginner?
1. Read `README.md` (main course overview)
2. Complete Module 1 exercises
3. Work through Module 2 simple demo
4. Ask for help if stuck!

### Some Python Experience?
1. Skim `README.md`
2. Jump to Module 2 (API Access)
3. Build on your existing knowledge
4. Try the advanced examples

### Advanced Student?
1. Review all module READMEs quickly
2. Start building final project early
3. Experiment with combining modules
4. Help classmates!

---

## 🚀 Quick Command Reference

### Module 1
```bash
cd Module1_InputProcessOutput
python exercises.py
```

### Module 2
```bash
cd Module2_DataGovAPI
cd MTRexamples
python mtr_api_test.py
```

### Module 3
```bash
cd Module3_WebCrawler_NBA
python nba_crawler.py
```

### Module 4
```bash
cd Module4_LLM_API
export HKBU_GENAI_API_KEY="your_key_here"
python llm_client.py
```

---

## 💡 Common First-Time Issues

### Problem: `pip: command not found`
**Solution**: Use `pip3` instead: `pip3 install requests`

### Problem: `Permission denied`
**Solution**: Use user install: `pip install --user requests`

### Problem: Libraries install but import fails
**Solution**: Ensure you're using the same Python version:
```bash
python --version
python -m pip install requests
```

### Problem: Module not found error
**Solution**: Install in the correct environment:
```bash
which python
which pip
# Make sure both point to the same Python installation
```

---

## 📖 Learning Path

```
Day 1: Module 1 (IPO Foundation)
       ↓
Day 2-3: Module 2 (API Data Access)
       ↓
Day 4-6: Module 3 (Web Crawling)
       ↓
Day 7-8: Module 4 (LLM Integration)
       ↓
Day 9-14: Final Project
```

---

## ✅ First Day Checklist

- [ ] Install Python 3.8+
- [ ] Install required libraries
- [ ] Read main README.md
- [ ] Complete Module 1 exercises
- [ ] Plan your final project idea

---

## 🎓 Success Tips

1. **Don't skip Module 1** - IPO thinking is foundational
2. **Test code frequently** - Run after every change
3. **Read error messages** - They tell you what's wrong!
4. **Start simple** - Get basic version working first
5. **Ask questions early** - Don't struggle alone

---

## 📞 Getting Help

1. Check module README files
2. Review code examples
3. Ask classmates
4. Post in discussion forum
5. Attend office hours

---

## 🏆 Your First Win

Complete this to verify everything works:

```python
# Save as test_setup.py
import requests
import pandas as pd
import matplotlib.pyplot as plt

print("✓ Requests library ready")
print("✓ Pandas library ready")
print("✓ Matplotlib library ready")

# Test IPO model
# INPUT
numbers = [1, 2, 3, 4, 5]

# PROCESS
average = sum(numbers) / len(numbers)

# OUTPUT
print(f"✓ IPO Model works! Average: {average}")
```

Run it:
```bash
python test_setup.py
```

If you see all checkmarks (✓), you're ready to go! 🎉

---

**Next Step**: Open `Module1_InputProcessOutput/README.md` and start learning!

