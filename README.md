# A/B Testing Marketing Campaigns

## Project Overview
This project analyzes **Control vs Test marketing campaigns** to evaluate which strategy performs better.  
The dataset comes from two CSV files: `control.csv` and `test.csv`.  

This project delivers the full A/B testing pipeline—from data cleaning and KPI setup to statistical tests and confidence intervals—so you can make a clear, data-driven decision.
---

## Workflow

1. **Data Loading & Renaming**  
   - Load control & test CSVs.  
   - Rename columns to a consistent, readable schema (e.g., amount_spent, impressions, reach, clicks, purchases) so merging and analysis are straightforward.
2. **Data Cleaning & Preparation**  
   - Parse campaign dates (`pd.to_datetime`).  
   - Handle missing values consistently:  
     - **Numeric columns:** fill with the column mean, then round count-like fields to integers.
     -  **Categorical columns:** fill with the mode (most frequent value).
   - Apply sanity checks:  
     - `clicks ≤ impressions`  
     - `purchases ≤ clicks`  
     - `reach ≤ impressions`  
     - No negative values.



3. **Feature Engineering (KPIs)**  
   - CTR (Click-Through Rate) = clicks / impressions
   - CAC (cost per acquisition) = spend / purchases  
   - CR (Conversion Rate) = purchases / reach 
   - CPM (Cost per 1000 impressions)  
   - CPC (Cost per click)  
   - CPA (Cost per acquisition)


4. **Align Overlapping Periods**  
   - Compare campaigns on the same dates only (overlapping period). 

5. **Exploratory Data Analysis (EDA)**  
   - Bar chart of campaign totals (spend, impressions, reach, clicks, purchases).
   - Line charts over time (CTR, CR, spend).
   - Scatter checks (e.g., clicks vs impressions, purchases vs reach).
   - Correlation heatmaps by campaign. 




6. **Statistical Testing**  
   - Two-proportion z-tests on totals for CTR (clicks/impressions) and CR (purchases/reach).
   - Report p-values for significance. 

7. **Confidence Intervals & Lift %**  
   - 95% CIs for CTR & CR.
   - Relative lift (Test vs Control).
   - Clear, human-readable conclusion (e.g., “Test CR is +64% higher and statistically significant”).


**Conclusion:**  
- CTR: Test ≈ 8.09%, Control ≈ 4.89% → +65% lift, p < 0.001.
- CR: Test ≈ 0.97%, Control ≈ 0.59% → +64% lift, p < 0.001.
- CAC: Control ≈ 4.38, Test ≈ 4.92 (≈ +12% higher for Test).

---

## Takeaway
- Test wins on efficiency (higher CTR & CR, statistically significant).
- Control wins on volume / lower CAC.
- Practical recommendation: Use Test for conversion-focused spend; use Control for broad, lower-cost scale—or run a hybrid based on goals.

---

## Tools Used
- Python, Pandas, NumPy  
- Plotly (interactive visualizations)  
- Statistical testing (two-proportion z-tests, confidence intervals)


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


