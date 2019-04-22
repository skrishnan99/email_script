# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACfe3f81c3a2cd6eccfd1ac3a8f2449584'
auth_token = '8ba90a5067ff1ec9e5ecc22397e6c999'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='yeet',
         from_='+19093219750',
         to='+19096156153'
     )

print(message.sid)


# def send_text(msg=None, receivers=None):