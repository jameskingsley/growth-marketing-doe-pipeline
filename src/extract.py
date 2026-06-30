import pandas as pd
import numpy as np

# Setup the 16 combinations using real marketing text names instead of -1 and +1
raw_combinations = {
    'Ad_Hook':     ['Scarcity/FOMO', 'Scarcity/FOMO', 'Scarcity/FOMO', 'Benefit-Driven', 'Benefit-Driven', 'Benefit-Driven', 'Benefit-Driven', 'Benefit-Driven', 'Scarcity/FOMO', 'Scarcity/FOMO', 'Benefit-Driven', 'Benefit-Driven', 'Scarcity/FOMO', 'Benefit-Driven', 'Benefit-Driven', 'Scarcity/FOMO'],
    'Visual_Type': ['Static Image', 'Static Image', 'Short Video', 'Short Video', 'Short Video', 'Static Image', 'Static Image', 'Static Image', 'Short Video', 'Static Image', 'Short Video', 'Short Video', 'Short Video', 'Static Image', 'Static Image', 'Static Image'],
    'CTA_Text':    ['Learn More', 'Learn More', 'Get Started Now', 'Learn More', 'Learn More', 'Get Started Now', 'Learn More', 'Learn More', 'Learn More', 'Get Started Now', 'Get Started Now', 'Get Started Now', 'Learn More', 'Learn More', 'Get Started Now', 'Get Started Now'],
    'Audience':    ['Established Managers', 'Young Professionals', 'Established Managers', 'Young Professionals', 'Established Managers', 'Established Managers', 'Young Professionals', 'Established Managers', 'Young Professionals', 'Young Professionals', 'Young Professionals', 'Established Managers', 'Established Managers', 'Young Professionals', 'Young Professionals', 'Established Managers'],
    'Incentive':   ['10% Discount', 'Free Trial Extension', '10% Discount', 'Free Trial Extension', '10% Discount', '10% Discount', '10% Discount', 'Free Trial Extension', '10% Discount', '10% Discount', '10% Discount', 'Free Trial Extension', 'Free Trial Extension', 'Free Trial Extension', 'Free Trial Extension', 'Free Trial Extension']
}

df_raw_mock = pd.DataFrame(raw_combinations)

# Add realistic messy platform columns (Spend and Conversions instead of a pre-calculated CPA)
np.random.seed(42)
df_raw_mock['Total_Spend'] = np.random.uniform(450, 550, 16) 

# Generate mock conversions where Short Video and Free Trial perform better
base_conversions = 20
visual_modifier = np.where(df_raw_mock['Visual_Type'] == 'Short Video', 8, -4)
incentive_modifier = np.where(df_raw_mock['Incentive'] == 'Free Trial Extension', 10, -5)
noise = np.random.randint(-2, 3, 16)

df_raw_mock['Conversions'] = base_conversions + visual_modifier + incentive_modifier + noise

# Save it directly into the data/raw directory
df_raw_mock.to_csv('data/raw/fb_ads_export_june2026.csv', index=False)
print("Successfully generated mock raw export in data/raw/fb_ads_export_june2026.csv")