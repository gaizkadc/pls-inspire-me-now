import random


def parse_quotes(file_name, logger):
    logger.info('parsing exercises from {}'.format(file_name))

    quotes = []

    try:
        quotes_file = open(file_name, 'r')
        quotes_data = quotes_file.readlines()

        for quote in quotes_data:
            quotes.append(quote.strip('\n'))

    except ModuleNotFoundError as error:
        logger.error('something went wrong')
        logger.error(error)

    logger.info('quotes parsed')

    return list(dict.fromkeys(quotes))


def check_quotes_len(quotes, max_quote_len, logger):
    logger.info('checking quotes len')

    for quote in quotes:
        if len(quote) > max_quote_len:
            logger.error('quote too long: ' + quote)
            return False

    return True


def create_quote(quotes, max_line_len, max_quote_len, logger):
    logger.info('creating quote')

    quote = ''
    line = ''

    while True:
        if len(quote) >= max_quote_len:
            break
        else:
            random.shuffle(quotes)
            new_quote = quotes.pop(0)

            if len(quote) == 0:
                line = new_quote
                quote += line
            else:
                if len(line + new_quote) > max_line_len:
                    line = '\n' + new_quote
                    quote += line
                else:
                    line += ' ' + new_quote
                    quote += ' ' + new_quote

    return quote
