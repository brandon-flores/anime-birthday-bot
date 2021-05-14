import tweepy
import logging
import time

from configs.conf import create_api

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def tweet_birthday(api):
    logger.info('Tweeting birthdays')
    # api.update_status('This is my initial tweet. Hello world!')
    api.update_status('New tweet!')


def main():
    api = create_api()
    tweet_birthday(api)
    # while True:
    #     logger.info("Waiting...")
    #     time.sleep(60)


if __name__ == "__main__":
    main()
