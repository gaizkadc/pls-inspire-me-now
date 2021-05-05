import twitter_utils
import utils
import quote_utils
import img_utils


# create a logger
logger = utils.get_logger()
logger.info('pls-inspire-me-now started')

# parse quotes from included file quotes.txt
quotes_file_name = 'quotes.txt'
max_line_len = 28
max_quote_len = 120

quotes = quote_utils.parse_quotes(quotes_file_name, logger)

if quote_utils.check_quotes_len(quotes, max_line_len, logger):
    quote = quote_utils.create_quote(quotes, max_line_len, max_quote_len, logger)
    quote_img = img_utils.create_quote_img(quote, logger)

    twitter_utils.tweet_quote(quote_img, quote, logger)
