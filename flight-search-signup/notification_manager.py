import os
import smtplib

import requests
from dotenv import load_dotenv

load_dotenv()

class NotificationManager:

    def __init__(self):
        self.discord_webhook = os.getenv("DISCORD_WEBHOOK")
        self.origin_email = os.getenv("MY_EMAIL")
        self.email_auth = os.getenv("EMAIL_AUTH")
        self.smtp = os.getenv("SMTP_SERVER")


    def send_discord_update(self, message):

        requests.post(self.discord_webhook, json={"content": message})

    def send_email(self, message, user):
        with smtplib.SMTP(self.smtp) as connection:
            connection.starttls()
            connection.login(user=self.origin_email, password=self.email_auth)
            connection.sendmail(
                from_addr=self.origin_email,
                to_addrs=user,
                msg=f"Subject: Low Price Flight Alert!\n\n{message}"
            )