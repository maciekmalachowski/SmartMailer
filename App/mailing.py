import os
from dotenv import load_dotenv
import yaml
import smtplib
from email.mime.text import MIMEText
from llama_index.core.tools import FunctionTool
from data_manager import reload_data, company_df

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
        msg['Subject'] = email_data.get("Subject")

        if isinstance(receiver_email, (list, tuple)):
            for email in receiver_email:
                msg['To'] = email
                # Send the email
                try:
                    with smtplib.SMTP("smtp.gmail.com", 587) as server:
                        server.starttls()
                        server.login(EMAIL, PASSWORD)
                        server.sendmail(EMAIL, email, msg.as_string())
                        # Update the send status to True where 'Company_email' matches the specified email
                        updated_df = company_df.copy()
                        updated_df.loc[updated_df['Company_email'] == email, 'Send_status'] = True

                        # Save the updated dataframe back to the Excel file
                        data_path = os.path.join("data", "company_data.xlsx")
                        updated_df.to_excel(data_path, index=False)
                        reload_data()
                    return f"Email sent to: {email}."
                except:
                    return f"Email {email} is not valid."
        else:
            return f"Given email has faulty type."


# Create the engine to send emails
send_email_engine = FunctionTool.from_defaults(
    fn=send_email,
    name="send_email_tool",
    description=(
    "This tool sends emails to one or more recipients and updates the 'Send_status' in the company data after successfully sending the email."
    "Provide the recipient email addresses as a list, even if there's only one email."
    "The tool ensures that the email is sent, and upon success, marks the respective company's 'Send_status' status as updated."
    )
)