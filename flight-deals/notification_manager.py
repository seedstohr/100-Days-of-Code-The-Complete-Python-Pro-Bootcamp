import os
import requests
from dotenv import load_dotenv

load_dotenv()

class NotificationManager:

    def __init__(self):
        self.discord_webhook = os.getenv("DISCORD_WEBHOOK")

    def send_discord_update(self, message):

        requests.post(self.discord_webhook, json={"content": message})