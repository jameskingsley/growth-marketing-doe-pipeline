# Growth Engineering Framework: Multi-Factor Design of Experiments (DoE)

An enterprise-grade optimization engine that utilizes a fractional factorial design to systematically isolate creative and incentive drivers while minimizing marketing Cost Per Acquisition (CPA). This repository contains the end-to-end pipeline—moving from historical feature screening to predictive live tracking using Statistical Process Control (SPC).

---

## Key Business Outcomes
* **CPA Minimization:** Systematically identified the optimal channel configuration, dropping the target baseline from an unstable historical average of **$35.00** to a validated, highly efficient mean of **$8.49**.
* **Testing Overhead Reduction:** Proved that Hooks, CTAs, and Target Demographics do not statistically shift the needle on this channel, safely removing **60%** of future creative testing surface area.
* **Risk Mitigation:** Deployed automated daily process control boundaries utilizing **95% Prediction Intervals** to detect live campaign performance drift instantly.

---

## Repository Architecture & Workflow

The pipeline is split into a modular, production-grade architecture to maintain strict data engineering separation between model screening, forward-looking validation, and visual artifacts:

```text
├── data/
│   ├── processed/
│   │   └── cleaned_marketing_matrix.csv     
│   └── raw/                                 
├── notebooks/
│   ├── 01_exploratory_data.ipynb           
│   ├── 02_confirmation_run_validation.ipynb 
│   ├── interaction_effect_chart.png         
│   └── production_monitoring_chart.png      
├── src/
│   ├── __init__.py                          
│   ├── clean_data.py                        
│   ├── data_pipeline.py                     
│   ├── extract.py                           
│   └── stats_models.py                      
└── README.md   

1. Screening Phase (exploratory_data.ipynb)
Model Formulation: Fits an Ordinary Least Squares (OLS) model against centered contrast vectors (−1, +1) to extract clean main effects.

Pipeline Integrity: Validates classical linear regression constraints natively via statistical diagnostic checks:

Shapiro-Wilk Test: Confirms residual normality (p=0.1272).

Levene’s Test: Verifies homoscedasticity across cohorts (p=0.0952).

Variance Screening: Employs multi-factor Type-II ANOVA testing (α=0.05) to isolate statistically significant cost drivers:

Highly Significant: Visual (p=0.000671) and Offer (p=0.000214).

Background Noise: Hook, CTA, and Demo (all p>0.05).

2. Validation & Deployment (confirmation_run_validation.ipynb)
Predictive Inference: Extracts a 95% Prediction Interval (obs=True) to establish true operational variance bounds (−$7.77 to $24.75) around the optimized expected mean of $8.49.

Power Analysis Sizing: Leverages Cohen's d to measure effect magnitude. Due to a massive derived effect size (d=5.560), the power equations determine that a minimum conversion scale of only 10 sample points is required to confirm the run with 80% statistical power (α=0.05).

Live Automated Tracking: Ingests incoming production data streams, routes them through programmatic business-logic guard check conditionals, and exports a production-ready Process Control Chart.

###### System Visualization
Creative Optimization Matrix
The interaction analysis shows the stark cost cliff where our strategy succeeds. Shifting from Static Images to Short Videos reduces costs drastically, with the absolute optimal performance achieved when anchoring to a Free Trial Extension.

Production Process Control Chart
The live confirmation stream fluctuates smoothly within our pre-calculated statistical bounds. The visual rendering engine employs an automated max(0, ci_lower) clamp to keep the lower control limit locked cleanly at a real-world bound of $0.00.

###### Operational Deployment Runbook
Prerequisites
Ensure your local environment is running Python 3.10+ with standard data science packages installed. Containerization tools (e.g., Docker) are explicitly avoided to maximize local bare-metal execution speeds.

Bash
pip install pandas numpy matplotlib seaborn statsmodels scipy
Execution
Run the full optimization suite sequentially to update underlying diagnostic reports:

Open and execute notebooks/01_exploratory_data.ipynb to update screening baselines and output the interaction asset.

Open and execute notebooks/02_confirmation_run_validation.ipynb to refresh the live monitoring control chart.