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
BEARER_TOKEN = environ.get("BEARER_TOKEN")
CLIENT_ID = environ.get("CLIENT_ID")
CLIENT_SECRET = environ.get("CLIENT_SECRET")

def post_tweet(client, message: str):
    """Post a tweet using the provided client and message."""
    try:
        response = client.create_tweet(text=message, user_auth=True)
        print(f"Successfully posted tweet with ID: {response.data.id}")
    except Exception as e:
        print(f"Error occurred: {e}")
        print(traceback.format_exc())

def main():
    """Main function to execute the script."""
    # Check if all keys are loaded correctly
    if not all([API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, BEARER_TOKEN]):
        print("One or more environment variables are missing.")
        exit()

    oauth2_user_handler = tweepy.OAuth2UserHandler(
        client_id = API_KEY, 
        redirect_uri = "https://twitter.com/botanybound",
        scope = ["read", "write"],  
        client_secret = API_SECRET_KEY  
    )

    # Generate the authorization URL to redirect the user
    auth_url = oauth2_user_handler.get_authorization_url()
    print(f"Please go to this URL and authorize the app: {auth_url}")

    # Get the code from the callback URL after the user authorizes the app
    code = input("Enter the code from the callback URL: ")

    # Fetch the user's access token using the provided code
    oauth2_user_handler.fetch_access_token(code)

    # Set up the client using the user's access token
    client = tweepy.Client(oauth2_user_handler=oauth2_user_handler)

    post_tweet(client, "Using Tweepy with Twitter API v2 with OAuth2 for the first time!")

if __name__ == "__main__":
    main()
