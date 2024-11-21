import os
import pandas as pd

# Path to the data file
data_path = os.path.join("data", "company_data.xlsx")

# Global DataFrame to be used by all modules
company_df = pd.read_excel(data_path)

def reload_data():
    """Reload the data from the Excel file."""
    global company_df
    company_df = pd.read_excel(data_path)
