import os
import sys
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

call = client.calls.create(
                        twiml=f'<Response><Pause length="2"/><Say>{sys.argv[1]}</Say><Hangup/></Response>',
                        to='+18132960491',
                        from_=os.environ['TWILIO_NUMBER']
                        )
