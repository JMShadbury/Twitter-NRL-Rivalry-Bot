import requests
from requests_oauthlib import OAuth1
from util.config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

def upload_media(media_data):
    """Uploads media to Twitter and returns the media ID for use in tweets."""
    url = "https://upload.twitter.com/1.1/media/upload.json"
    auth = OAuth1(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    files = {'media': media_data}
    response = requests.post(url, files=files, auth=auth)
    if response.status_code == 200:
        return response.json()['media_id_string']
    else:
        raise Exception(f"Media could not be uploaded: {response.text}")

def post_tweet(tweet_text, media_id=None):
    """Posts a tweet with or without media."""
    url = "https://api.twitter.com/2/tweets"
    auth = OAuth1(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    headers = {"Content-Type": "application/json"}
    payload = {"text": tweet_text, "media_ids": media_id} if media_id else {"text": tweet_text}
    response = requests.post(url, json=payload, headers=headers, auth=auth)
    if response.status_code == 201:
        return response.json()
    else:
        raise Exception(f"Tweet could not be posted: {response.text}")
