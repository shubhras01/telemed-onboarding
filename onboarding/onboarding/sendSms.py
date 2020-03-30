"""Functions for freshdesk api exposed to other modules."""
import configparser
from twilio.rest import Client

config = configparser.ConfigParser()['twilio']
config.read('freshdesk_secrets.ini')
ACCOUNT_SID = config['account_sid']
AUTH_TOKEN = config['auth_token']


client = Client(ACCOUNT_SID, AUTH_TOKEN)


def sendSms(to_number, message):
    message = client.messages.create(
        to=to_number, 
        from_="+12058523844",
        body=message)

    print(message.sid)
