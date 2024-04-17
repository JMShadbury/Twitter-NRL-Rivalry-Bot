import requests
from requests_oauthlib import OAuth1
from util.config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

class TweetManager:
    def __init__(self, logging):
        self.url = "https://api.twitter.com/2/tweets"
        self.auth = OAuth1(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        self.headers = {"Content-Type": "application/json"}
        self.logging = logging
        self.logging.info("Tweet Manager Initialized")
        self.logging.debug(f"URL: {self.url}")
        self.logging.debug(f"Headers: {self.headers}")

    def post_tweet(self, tweet_text):
        payload = {"text": tweet_text}
        response = requests.post(self.url, json=payload, headers=self.headers, auth=self.auth)
        if response.status_code == 201:
            return response.json()
        else:
            raise Exception(f"Tweet could not be posted: {response.text}")
