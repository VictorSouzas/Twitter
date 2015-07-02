import get_access_token
from requests_oauthlib import OAuth1
from status_update import status_up


consumer_key = ""
consumer_secret = ""

token, secret = get_access_token.main(consumer_key, consumer_secret)

def get_oauth(token, secret):
    oauth = OAuth1(consumer_key,
                client_secret=consumer_secret,
                resource_owner_key=token,
                resource_owner_secret=secret)
    return oauth

oauth = get_oauth(token,secret)
status = "testando api do twitter  com #python"
up_status = status_up(oauth, status)
print up_status.json()