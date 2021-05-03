import tweepy
import os
import locale
import datetime
import random


def get_twitter_credentials(logger):
    logger.info('getting twitter credentials')

    try:
        logger.info('retrieving twitter credentials from settings')
        import settings
        consumer_key = settings.TWITTER_CONSUMER_KEY
        consumer_secret = settings.TWITTER_CONSUMER_SECRET
        access_token = settings.TWITTER_ACCESS_TOKEN
        access_token_secret = settings.TWITTER_ACCESS_TOKEN_SECRET
    except ModuleNotFoundError as error:
        logger.info('unable to import settings')
        logger.info(error)
        consumer_key = os.getenv('TWITTER_CONSUMER_KEY')
        consumer_secret = os.getenv('TWITTER_CONSUMER_SECRET')
        access_token = os.getenv('TWITTER_ACCESS_TOKEN')
        access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

    credentials = {
        'consumer_key': consumer_key,
        'consumer_secret': consumer_secret,
        'access_token': access_token,
        'access_token_secret': access_token_secret
    }

    logger.info('twitter credentials retrieved')

    return credentials


def twitter_login(credentials, logger):
    logger.info('logging in twitter')

    auth = tweepy.OAuthHandler(credentials['consumer_key'], credentials['consumer_secret'])
    auth.set_access_token(credentials['access_token'], credentials['access_token_secret'])
    api = tweepy.API(auth, wait_on_rate_limit=True)

    logger.info('logged in twitter')

    return api


def tweet_quote(img_path, quote, logger):
    logger.info('tweeting quote')

    twitter_credentials = get_twitter_credentials(logger)
    twitter_api = twitter_login(twitter_credentials, logger)

    hashtags = '\n#inpirational\n#inspirationaladvice'

    tweet_text = quote + hashtags

    twitter_api.update_with_media(img_path, status=tweet_text)
    logger.info(tweet_text)
    logger.info('quote img: ' + img_path)

    logger.info('quote tweeted')
