import smtplib
from email.mime.text import MIMEText
from llama_index.core.tools import FunctionTool
import pandas as pd
import os
import yaml
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

def send_email(receiver_name):
    # Load the company data from Excel
    data_path = os.path.join("data", "company_data.xlsx")
    df = pd.read_excel(data_path)
    
    # Ensure only one matching email is found
    receiver_email_series = df.loc[df["Company_name"] == receiver_name, "Company_email"]
    if receiver_email_series.shape[0] != 1:
        return f"Error: Multiple or no matching email addresses found for {receiver_name}."
    
    receiver_email = receiver_email_series.iloc[0]

    # Load email content
    with open(os.path.join("data", "email.md"), "r") as file:
        content = file.read().split("---")[1]
        email_data = yaml.safe_load(content)

    # Compose the email
    msg = MIMEText(email_data.get("Message"))
    msg['From'] = EMAIL
    msg['To'] = receiver_email
    msg['Subject'] = email_data.get("Subject")

    # Send the email
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.sendmail(EMAIL, receiver_email, msg.as_string())
    
    return "Email sent"

# Create the tool to send emails
email_engine = FunctionTool.from_defaults(
    fn=send_email,
    name="email_sender",
    description="This tool is used to send emails to a specified receiver provided by user."
)
