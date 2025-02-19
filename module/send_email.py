from dotenv import load_dotenv
import os
import smtplib, ssl

load_dotenv()

username = os.getenv('SENDER_EMAIL')
password = os.getenv('SENDER_PASSWORD')
receiver = os.getenv('RECEIVER_EMAIL') if os.getenv('RECEIVER_EMAIL') else username

host = "smtp.gmail.com"
port = 465
context = ssl.create_default_context()

message_body = f"""\
From: Leonidas <{username}>
Subject: Test Email from Streamlit Company Portfolio Practice
Company test email
"""


def send_email(message_body_param=message_body):
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        result = server.sendmail(username, receiver, message_body_param)
        print(f"Email sent successfully! Result: {result}")  # empty dict expected


if __name__ == '__main__':
    send_email()
