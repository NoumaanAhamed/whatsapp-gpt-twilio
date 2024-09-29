from dotenv import load_dotenv
load_dotenv()
import os

from twilio.rest import Client

account_sid = os.getenv('TWILIO_ACCOUNT_SID') 
auth_token = os.getenv('TWILIO_AUTH_TOKEN')

client = Client(account_sid, auth_token)

from_whatsapp_number='whatsapp:+14155238886'
to_whatsapp_number='whatsapp:' + os.getenv('MY_PHONE_NUMBER')

message = client.messages.create(
  body='Hello from Noumaan!',
  from_=from_whatsapp_number,
  to=to_whatsapp_number,
)

print(message)