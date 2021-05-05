import twitter_utils
import utils


# create a logger
logger = utils.get_logger()
logger.info('pimn-autolike started')

# Authenticate
twitter_credentials = twitter_utils.get_twitter_credentials(logger)
twitter_api = twitter_utils.twitter_login(twitter_credentials, logger)

# Get my Twitter ID
twitter_user = twitter_api.me()
twitter_id = twitter_user.id

# Get relevant tweets
search_terms = ['inspirational', 'inspirational advice', '#inspirational', '#inspirationaladvice']
inspirational_tweets = twitter_utils.search_tweets(search_terms, twitter_api, twitter_id, logger)

# Like relevant tweets
twitter_utils.like_tweets(inspirational_tweets, logger)
