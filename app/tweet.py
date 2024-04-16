import requests
from requests_oauthlib import OAuth1
from util.config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

def post_tweet(tweet_text):
    url = "https://api.twitter.com/2/tweets"
    auth = OAuth1(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    headers = {
        "Content-Type": "application/json"
    }
    payload = {"text": tweet_text}
    response = requests.post(url, json=payload, headers=headers, auth=auth)
    if response.status_code == 201:
        return response.json()
    else:
        raise Exception("Tweet could not be posted: " + response.text)