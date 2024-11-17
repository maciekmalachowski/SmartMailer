import os
import yaml
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from llama_index.core.tools import FunctionTool

# Load environmental variables
load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

def send_email(receiver_email):
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
        return f"Email sent to: {receiver_email}"

            
# Create the engine to send emails
send_email_engine = FunctionTool.from_defaults(
    fn=send_email,
    name="send_email_tool",
    description=(
        "This tool is used to send emails to one or more specified receiver emails. "
    )
)