from decouple import config
from urllib.parse import quote_plus
from requests_oauthlib import OAuth1Session
import json


CONSUMER_KEY=config('consumer_key')
CONSUMER_SECRET=config('consumer_secret')
ACCESS_TOKEN=config('access_token')
ACCESS_TOKEN_SECRET=config('access_token_secret')
YOUR_DOMAIN= "https://dmrobot.herokuapp.com" #config('website_domain') 
#The domain heroku gave you. Yes the entire url. e.g. "https://catfactbot-twitter.herokuapp.com"
YOUR_DEV_ENVIRONMENT_LABEL="dmrobot" #config('dev_env_label') 
#This is the Label you gave to your Account Activity API Environment when you registered your app.  

twitter = OAuth1Session(CONSUMER_KEY,
                        client_secret=CONSUMER_SECRET,
                        resource_owner_key=ACCESS_TOKEN,
                        resource_owner_secret=ACCESS_TOKEN_SECRET)


webhook_endpoint = quote_plus(YOUR_DOMAIN)
url = 'https://api.twitter.com/1.1/account_activity/all/{YOUR_DEV_ENVIRONMENT_LABEL}/' #


def register_webhook(url,twitter,webhook_endpoint):
    url+=f'webhooks.json?url={webhook_endpoint}'
    response = twitter.post(url)
    print(response)

def subscribe_to_user_activity(url,twitter):
    url+=f'subscriptions.json'
    response = twitter.post(url)
    print(response)

if __name__ == '__main__':
    register_webhook(url,twitter,webhook_endpoint)
    subscribe_to_user_activity(url,twitter)