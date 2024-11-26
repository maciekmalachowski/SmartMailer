import os
import pandas as pd
from llama_index.core.tools import FunctionTool
from data_manager import reload_data, company_df

# Function to add new records to the dataframe
def add_record(name, email):
    # Add a new record (new row)
    new_record = {'Company_name': name, 'Company_email': email, 'Send_status': False}
    updated_df = pd.concat([company_df, pd.DataFrame([new_record])], ignore_index=True)

    # Save the updated dataframe back to the Excel file
    data_path = os.path.join("data", "company_data.xlsx")
    updated_df.to_excel(data_path, index=False)

    # Reload the dataframe after the update
    reload_data()

    return f"New record {name}, {email} added successfully."

# Function to delete a record from the dataframe based on the company name
def delete_record(name):
    # Check if the record exists
    if name not in company_df['Company_name'].values:
        return f"Company with name {name} not found."

    # Remove the record
    updated_df = company_df[company_df['Company_name'] != name]

    # Save the updated dataframe back to the Excel file
    data_path = os.path.join("data", "company_data.xlsx")
    updated_df.to_excel(data_path, index=False)

    # Reload the dataframe after the update
    reload_data()

    return f"Record for {name} deleted successfully."

# Function to update the email for a given company name
def update_email(company_name, new_email):
    # Check if the company name exists in the dataframe
    if company_name not in company_df['Company_name'].values:
        return f"Company with name {company_name} not found."

    # Update the email for the given company
    updated_df = company_df.copy()
    updated_df.loc[updated_df['Company_name'] == company_name, 'Company_email'] = new_email
    updated_df.loc[updated_df['Company_name'] == company_name, 'Send_status'] = False

    # Save the updated dataframe back to the Excel file
    data_path = os.path.join("data", "company_data.xlsx")
    updated_df.to_excel(data_path, index=False)

    # Reload the dataframe after the update
    reload_data()

    # Return a success message with the updated email
    updated_email = updated_df.loc[updated_df['Company_name'] == company_name, 'Company_email'].iloc[0]
    return f"Email for {company_name} updated successfully to {updated_email}."

# Function to update whether an email has been sent for a given company name
def change_send_status(company_name, send_value):
    # Check if the company name exists in the dataframe
    if company_name not in company_df['Company_name'].values:
        return f"Company with name {company_name} not found."

    # Update the email for the given company
    updated_df = company_df.copy()
    for name in company_name:
        updated_df.loc[updated_df['Company_name'] == name, 'Send_status'] = send_value

    # Save the updated dataframe back to the Excel file
    data_path = os.path.join("data", "company_data.xlsx")
    updated_df.to_excel(data_path, index=False)

    # Reload the dataframe after the update
    reload_data()

    # Return a success message with the updated email
    return f"Whether sent for {company_name} updated successfully."

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

# Create the engine to update whether an email has been sent
change_if_sent_engine = FunctionTool.from_defaults(
    fn=change_send_status,
    name="change_send_status_tool",
    description="This tool updates the 'Send_status' for a specific company in the company data based on the company name. Provide the company names as a list, even if there's only one name."
)