import os
import requests
from dotenv import load_dotenv
import smtplib, ssl

load_dotenv()

NEWS_API_URL = os.getenv("NEWS_API_URL")
SMTP_ACCOUNT_EMAIL_ADDRESS = os.getenv("SMTP_ACCOUNT_EMAIL_ADDRESS")
SMTP_ACCOUNT_EMAIL_PASSWORD = os.getenv("SMTP_ACCOUNT_EMAIL_PASSWORD")
SMTP_RECEIVER_EMAIL_ADDRESS = os.getenv("SMTP_RECEIVER_EMAIL_ADDRESS")


"""fn to send email to the hardcoded user using hardcoded account"""
def send_email(message):
    
    host = "smtp.gmail.com"
    port = 465

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(SMTP_ACCOUNT_EMAIL_ADDRESS, SMTP_ACCOUNT_EMAIL_PASSWORD)
        server.sendmail(SMTP_ACCOUNT_EMAIL_ADDRESS, SMTP_RECEIVER_EMAIL_ADDRESS, message)


response = requests.get(NEWS_API_URL)
content = response.json()

print(content['articles'][0])