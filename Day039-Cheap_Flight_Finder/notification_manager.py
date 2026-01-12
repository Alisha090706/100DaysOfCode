import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

class NotificationManager:

    def __init__(self):
        self.client = Client(os.getenv('TWILIO_SID'), os.getenv("TWILIO_AUTH_TOKEN"))

    def send_sms(self, message_body):
        message = self.client.messages.create(
            from_=os.getenv("TWILIO_VIRTUAL_NUMBER"),
            body=message_body,
            to=os.getenv("TWILIO_VIRTUAL_NUMBER")
        )
        # Prints if successfully sent.
        print(message.sid)
