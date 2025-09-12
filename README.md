# A/B Testing Marketing Campaigns

## Project Overview
This project analyzes **Control vs Test marketing campaigns** to evaluate which strategy performs better.  
The dataset comes from two CSV files: `control_group.csv` and `test_group.csv`.  

While many tutorials stop at **renaming columns and making pie charts**, this project goes further by applying **data cleaning, KPI engineering, statistical tests, and confidence intervals** for a complete A/B testing workflow.  

---

## Workflow

1. **Data Loading & Renaming**  
   - Load control & test CSVs.  
   - Standardize schema with clear, human-readable column names.  

2. **Data Cleaning & Preparation**  
   - Parse campaign dates (`pd.to_datetime`).  
   - Handle missing values consistently:  
     - Counts (clicks, purchases, etc.) → filled with 0.  
     - Spend/impressions/reach → filled with mean.  
   - Apply sanity checks:  
     - `clicks ≤ impressions`  
     - `purchases ≤ clicks`  
     - `reach ≤ impressions`  
     - No negative values.  

3. **Feature Engineering (KPIs)**  
   - CTR (Click-Through Rate)  
   - CR (Conversion Rate)  
   - CPM (Cost per 1000 impressions)  
   - CPC (Cost per click)  
   - CPA (Cost per acquisition)  

4. **Align Overlapping Periods**  
   - Ensure both campaigns are compared only in the same time window.  

5. **Exploratory Data Analysis (EDA)**  
   - Scatter plots (Impressions vs Spend, Content vs Clicks, Cart vs Purchases).  
   - Pie charts comparing campaign totals.  
   - Line charts over time (CTR/CR trends).  

6. **Statistical Testing**  
   - Two-proportion z-tests for CTR & CR.  
   - p-values reported for statistical significance.  

7. **Confidence Intervals & Lift %**  
   - 95% confidence intervals for CTR & CR.  
   - Percentage lift from Control → Test.  
   - Clear, human-readable conclusion (e.g., *“Test CR is +22% higher and statistically significant”*).  


**Conclusion:**  
- Conversion Rate: Test is **+22.22% higher** than Control (statistically significant).  
- CTR difference is **not significant** at α=0.05.  

---

## Executive Summary
- The **Test campaign** achieved a **22% lift in conversion rate** compared to the Control group, with statistical significance.  
- The **Click-Through Rate (CTR)** difference was minimal (+1.3%) and not statistically significant.  
- Marketing teams could use the **Control campaign** for broad awareness (higher reach and total purchases), while the **Test campaign** shows potential for more efficient targeted conversions.  
- Overall: **Control = volume winner**, **Test = efficiency winner**.   

---

## Tools Used
- Python, Pandas, NumPy  
- Plotly (interactive visualizations)  
- Statistical testing (z-tests, confidence intervals)  

---

## Quick Start

Clone this repo and run the notebook/script:

```bash
# 1. Clone the repo
git clone https://github.com/BMatewos/ab_testing_marketing.git 
cd ab_testing_marketing

# 2. (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the analysis (choose one)
# Option A: Jupyter Notebook
jupyter notebook A_B_Testing.ipynb

# Option B: Python script
python ab_testing.py


---


