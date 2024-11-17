import os
import pandas as pd
from llama_index.core.tools import FunctionTool

# Function to add new records to the dataframe
def add_record(name, email):
    # Load the existing DataFrame
    data_path = os.path.join("data", "company_data.xlsx")
    df = pd.read_excel(data_path)

    # Add a new record (new row)
    new_record = {'Company_name': name, 'Company_email': email}
    df = pd.concat([df, pd.DataFrame([new_record])], ignore_index=True)

    # Save the updated dataframe back to the Excel file
    df.to_excel(data_path, index=False)

    return f"New record for {name} added successfully."

# Function to delete a record from the dataframe based on the company name
def delete_record(name):
    # Load the existing DataFrame
    data_path = os.path.join("data", "company_data.xlsx")
    df = pd.read_excel(data_path)

    # Check if the record exists
    if name not in df['Company_name'].values:
        return f"Company with name {name} not found."

    # Remove the record
    df = df[df['Company_name'] != name]

    # Save the updated dataframe back to the Excel file
    df.to_excel(data_path, index=False)

    return f"Record for {name} deleted successfully."

# Function to update the email for a given company name
def update_email(company_name, new_email):
    # Load the existing DataFrame
    data_path = os.path.join("data", "company_data.xlsx")
    df = pd.read_excel(data_path)

    # Check if the company name exists in the dataframe
    if company_name not in df['Company_name'].values:
        return f"Company with name {company_name} not found."

    # Update the email for the given company
    df.loc[df['Company_name'] == company_name, 'Company_email'] = new_email

    # Save the updated dataframe back to the Excel file
    df.to_excel(data_path, index=False)

    return f"Email for {company_name} updated successfully."


# Create the engine to add a record
add_record_engine = FunctionTool.from_defaults(
    fn=add_record,
    name="add_record_tool",
    description="This tool adds a new record (company name and email) to the company data."
)

# Create the engine to delete a record
delete_record_engine = FunctionTool.from_defaults(
    fn=delete_record,
    name="delete_record_tool",
    description="This tool deletes a record from the company data based on the company name."
)

# Create the engine to update the email for a record
update_email_engine = FunctionTool.from_defaults(
    fn=update_email,
    name="update_email_tool",
    description="This tool updates the email address for a specific company in the company data based on the company name."
)

