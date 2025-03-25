import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()


class NotificationManager:

    def __init__(self):
        TWILIO_SID = os.environ["TWILIO_SID"]
        TWILIO_AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message_body):
        MY_PHONE_NUMBER = os.environ["MY_PHONE_NUMBER"]
        TWILIO_PHONE_NUMBER = os.environ["TWILIO_PHONE_NUMBER"]
        message = self.client.messages.create(
            from_=TWILIO_PHONE_NUMBER,
            body=message_body,
            to=MY_PHONE_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    # Is SMS not working for you or prefer whatsapp? Connect to the WhatsApp Sandbox!
    # https://console.twilio.com/us1/develop/sms/try-it-out/whatsapp-learn
    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_=f'whatsapp:{os.environ["TWILIO_WHATSAPP_NUMBER"]}',
            body=message_body,
            to=f'whatsapp:{os.environ["TWILIO_VERIFIED_NUMBER"]}',
        )
        print(message.sid)
