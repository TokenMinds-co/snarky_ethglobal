import os
import tweepy
from dotenv import load_dotenv
import time
import sys

load_dotenv(override=True)

# Twitter Creds Variable
TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

client = tweepy.Client(
    bearer_token=TWITTER_BEARER_TOKEN,
    consumer_key=TWITTER_API_KEY,
    consumer_secret=TWITTER_API_SECRET,
    access_token=TWITTER_ACCESS_TOKEN,
    access_token_secret=TWITTER_ACCESS_TOKEN_SECRET,
)


# Test function to post listed NFT on Twitter => LET'S USE THIS ONE FOR TESTING
def post_nft_on_twitter(content:str):
    """
    Market/Post NFT on X-Account

    Args:
        content (str):Content about the NFT to post

    """
    try:
        print(f"Posting NFT on Twitter...")

        tweet = client.create_tweet(text=content)
        tweet_id = tweet.data['id']

        print(f"Successfully posted tweet: {tweet.data}")
       
        print("Sleeping for 60 then check tweet performance")
        time.sleep(60)
        
        totalLikes = count_post_like(tweet_id)
        if(totalLikes > 1):
            return f"Lore is good, continue to mint NFT using this lore"
        else:
            print (f"Lore is bad, redeploy to create new lore")
            sys.exit()

    except tweepy.TweepyException as e:
        print(f"{str(e)}")
        return f"Error posting NFT on tweet: {str(e)}"

# Check Twitter Post Like
def count_post_like(tweetId: str):
    """
    Check number of likes for a specific tweet/post

    Args:
        tweetId (str): id of the post to be checked

    Returns:
        int: amount of likes
    """
    try:
        tweet = client.get_liking_users(id=tweetId, user_auth=True)
        print(tweet)
        likingUsers = tweet.data
        return len(likingUsers)

    except tweepy.TweepyException as e:
        print(f"{str(e)}")
        delete_twitter_post(tweetId)
        return f"Error posting tweet: {str(e)}"

# Real Function to post on Twitter
def delete_twitter_post(tweetId: str):
    """
    Delete a post on twitter

    Args:
        tweetId (str): id of the post to be deleted

    Returns:
        str: Status message about the tweet
    """
    try:

        tweet = client.delete_tweet(id=tweetId)
        return f"Successfully posted tweet: {tweet.data}"

    except tweepy.TweepyException as e:
        print(f"{str(e)}")
        return f"Error posting tweet: {str(e)}"
