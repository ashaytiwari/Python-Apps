import os
import requests
from dotenv import load_dotenv
import smtplib, ssl
from email.mime.text import MIMEText
import sys

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


"""fn to generate html template based on articles details"""
def generate_html_template(articles):
    
    if len(articles) == 0:
        return None
    
    main_template = ''

    for index, item in enumerate(articles[:10]):
        main_template = main_template + f"<h2>{index + 1}. {item['title']}</h2> \
          <p>{item['description']}</p> \
          <a href={item['url']}>{item['url']}</a>  <br /><br />"
    
    html_template = f"""\
      <html>
        <body>
          {main_template}
        </body>
      </html>
    """

    return html_template


subject = "Today's News"

response = requests.get(NEWS_API_URL)
content = response.json()

html_body = generate_html_template(content['articles'])

if html_body == None:
    print("No news found")
    sys.exit(1)

# Create the email
message = MIMEText(html_body, "html")
message["Subject"] = subject

send_email(message.as_string())