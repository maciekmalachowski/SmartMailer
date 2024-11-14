import smtplib
from email.mime.text import MIMEText
import os
import yaml
import json
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

def send_email():
    with open("App/email.md", "r") as file:
        content = file.read().split("---")[1]
        email_data = yaml.safe_load(content)

    with open("App/company_emails.json", "r") as file:
        company_data = json.load(file)

    for company in company_data:
        receiver = company.get('email')

        msg = MIMEText(email_data.get("Message"))
        msg['From'] = EMAIL
        msg['To'] = EMAIL
        msg['Subject'] = email_data.get("Subject")+f" {company.get('name')}"

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL, PASSWORD)
            server.sendmail(EMAIL, receiver, msg.as_string())
        print("Message sent")

if __name__ == "__main__":
    send_email()