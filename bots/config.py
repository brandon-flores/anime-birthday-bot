import tweepy
import logging
import os

logger = logging.getLogger()


def create_api():
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
    # consumer_key = os.getenv('ZWDrd0Aa80p1oEd6dUAs96sNk')  # CONSUMER_KEY
    # consumer_secret = os.getenv(  # CONSUMER_SECRET
    #     'kqZDbG8fnSGX1G1khgzl1tsiW8RlH9NtafHrJ5vd8vL6w2hLl4')
    # access_token = os.getenv(
    #     '1211469743493746688-2ppf6rBRwLSGe8UQBpzLxc8ReIPnUE')  # ACCESS_TOKEN
    # access_token_secret = os.getenv(  # ACCESS_TOKEN_SECRET
    #     'UlitYRU0VY04ecAhVopcksUyQNOYDgt9DqErBEMphzO8t')

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(
        auth, wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error('Error creating API', exc_info=True)
        raise e
    logger.info('API created')
    return api
