"""
src/clean_data.py
Production script to ingest raw ad network exports, transform them into
the structured mathematical design matrix, and output to the processed data layer.
"""
import os
import sys

# Ensure the script can see the root directory for imports
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from src.data_pipeline import process_live_marketing_data

def execute_cleaning_pipeline(raw_filename, processed_filename):
    """
    Executes the end-to-end extraction, transformation, and loading (ETL) 
    of the experimental marketing data.
    """
    # Build robust absolute paths using the verified project root
    raw_path = os.path.join(BASE_DIR, 'data', 'raw', raw_filename)
    processed_dir = os.path.join(BASE_DIR, 'data', 'processed')
    processed_path = os.path.join(processed_dir, processed_filename)
    
    print(f"Starting ETL: Ingesting raw data from {raw_path}...")
    
    if not os.path.exists(raw_path):
        print(f"Error: Raw file target '{raw_path}' not found.")
        print("Please check that the file exists in the data/raw/ directory.")
        sys.exit(1)
        
    try:
        # Run the transformation pipeline matrix mapping
        df_cleaned = process_live_marketing_data(raw_path)
        
        # Securely write the clean data out to the processed directory
        os.makedirs(processed_dir, exist_ok=True)
        df_cleaned.to_csv(processed_path, index=False)
        
        print("Data pipeline successful!")
        print(f"Cleaned matrix safely pushed to: {processed_path}")
        print(f"Dimensions verified: {df_cleaned.shape[0]} runs x {df_cleaned.shape[1]} columns.\n")
        
    except Exception as e:
        print(f"Critical Pipeline Failure: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    # Explicit file configuration matching the system setup
    TARGET_RAW_FILE = "fb_ads_export_june2026.csv"
    TARGET_PROCESSED_FILE = "cleaned_marketing_matrix.csv"
    
    execute_cleaning_pipeline(TARGET_RAW_FILE, TARGET_PROCESSED_FILE)