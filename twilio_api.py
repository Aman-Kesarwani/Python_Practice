from twilio.rest import Client
import config_key

client = Client(config_key.account_sid, config_key.auth_token)

call = client.messages.create(
    to=config_key.to,
    from_=config_key.from_,
    body="You are charged Rs. 15000. Thanks for optiong our service"
)
