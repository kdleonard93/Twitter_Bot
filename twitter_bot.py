import tweepy
import traceback
from os import environ
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

API_KEY = environ.get("API_KEY")
API_SECRET_KEY = environ.get("API_SECRET_KEY")
ACCESS_TOKEN = environ.get("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = environ.get("ACCESS_TOKEN_SECRET")
CLIENT_ID = environ.get("CLIENT_ID")
CLIENT_SECRET = environ.get("CLIENT_SECRET")

def post_tweet(api, message: str):
    try:
        tweet = api.update_status(message)
        print(f"Successfully posted tweet with ID: {tweet.id}")
    except tweepy.HTTPError as e:
        print(f"Error Code: {e.api_code}")
        print(f"Reason: {e.reason}")
        print(traceback.format_exc())


def main():
    # Check if all keys are loaded correctly
    if not all([API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET]):
        print("One or more environment variables are missing.")
        exit()

 
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY,ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # Instantiate the API object
    api = tweepy.API(auth)

    post_tweet(api, "Using Tweepy with Twitter API v2 using OAuth 1.0a User Context for the first time!")
    
    # Fetch and print the last 5 tweets from the home timeline
    try:
        tweets = api.home_timeline(count=5)
        for tweet in tweets:
            print(tweet.text)
    except tweepy.HTTPError as e:
        print(f"Error Code: {e.api_code}")
        print(f"Reason: {e.reason}")
    
    # Attempt to post a test tweet and print any error details
    try:
        api.update_status("Test tweet")
    except tweepy.HTTPError as e:
        print(f"Error Code: {e.api_code}")
        print(f"Reason: {e.reason}")


if __name__ == "__main__":
    main()
