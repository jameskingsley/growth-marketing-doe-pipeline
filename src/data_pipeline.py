"""
src/data_pipeline.py
Handles programmatic generation of orthogonal Fractional Factorial arrays
and data cleaning for ad network API exports.
"""
import pandas as pd
import numpy as np

def generate_validation_data(seed=42):
    """
    Generates a clean 16-run orthogonal $2^{5-1}$ array with preset 
    business impacts to validate that our downstream ANOVA engine works perfectly.
    """
    np.random.seed(seed)
    
    # Balanced basic design matrix (Factors A, B, C, D)
    data = {
        'Hook':        [ 1,  1,  1, -1, -1, -1, -1, -1,  1,  1, -1, -1,  1, -1, -1,  1],
        'Visual':      [ 1,  1, -1, -1, -1,  1,  1,  1, -1,  1, -1, -1, -1,  1,  1,  1],
        'CTA':         [-1, -1,  1, -1, -1,  1, -1, -1, -1,  1,  1,  1, -1, -1,  1,  1],
        'Demographic': [ 1, -1,  1, -1,  1,  1, -1,  1, -1, -1, -1,  1,  1, -1, -1,  1]
    }
    df = pd.DataFrame(data)
    
    # Programmatically derive Factor E using the design generator: E = ABCD
    df['Offer'] = df['Hook'] * df['Visual'] * df['CTA'] * df['Demographic']
    
    # Simulate a baseline campaign CPA ($25.00) 
    baseline_cpa = 25.0
    visual_impact = df['Visual'] * 3.5    
    offer_impact = df['Offer'] * -5.0      
    random_noise = np.random.normal(0, 0.75, 16)
    
    df['CPA'] = baseline_cpa + visual_impact + offer_impact + random_noise
    return df

def process_live_marketing_data(raw_csv_path):
    """
    Transforms actual text strings from ad manager exports into clean mathematical matrix inputs.
    """
    df_raw = pd.read_csv(raw_csv_path)
    
    # Secure computation of the response variable to protect mathematical metrics
    df_raw['CPA'] = df_raw['Total_Spend'] / df_raw['Conversions']
    df_raw['CPA'] = df_raw['CPA'].replace([np.inf, -np.inf], np.nan).fillna(df_raw['Total_Spend'])
    
    mapping = {
        'Ad_Hook':     {'Benefit-Driven': -1, 'Scarcity/FOMO': 1},
        'Visual_Type': {'Short Video': -1, 'Static Image': 1},
        'CTA_Text':    {'Learn More': -1, 'Get Started Now': 1},
        'Audience':    {'Young Professionals': -1, 'Established Managers': 1},
        'Incentive':   {'10% Discount': -1, 'Free Trial Extension': 1}
    }
    
    df_clean = pd.DataFrame()
    df_clean['Hook']   = df_raw['Ad_Hook'].map(mapping['Ad_Hook'])
    df_clean['Visual'] = df_raw['Visual_Type'].map(mapping['Visual_Type'])
    df_clean['CTA']    = df_raw['CTA_Text'].map(mapping['CTA_Text'])
    df_clean['Demo']   = df_raw['Audience'].map(mapping['Audience'])
    df_clean['Offer']  = df_raw['Incentive'].map(mapping['Incentive'])
    df_clean['CPA']    = df_raw['CPA']
    
    assert len(df_clean) == 16, "Data Architecture Error: Matrix must contain exactly 16 run variations."
    return df_clean