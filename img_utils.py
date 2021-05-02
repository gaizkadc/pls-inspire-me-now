import datetime
import os
import random

from PIL import Image, ImageFont, ImageDraw, ImageEnhance


def create_quote_img(quote, logger):
    logger.info('creating quote img')

    today = datetime.datetime.now()
    today_str = today.strftime('%Y%m%d')

    try:
        logger.info('retrieving imgs folder path from settings')
        import settings
        img_folder_path = settings.IMGS_FOLDER
    except ModuleNotFoundError as error:
        logger.error('unable to import settings')
        logger.error(error)
        img_folder_path = os.getenv('IMGS_FOLDER')

    if not os.path.exists(img_folder_path):
        os.makedirs(img_folder_path)

    resulting_img_path = img_folder_path + '/quote' + today_str + '.png'

    background_folder_path = 'backgrounds'
    background_path = get_background(background_folder_path)

    darken_img(background_path, resulting_img_path)

    text_color = (255, 255, 255)
    write_title(today_str, resulting_img_path, text_color, logger)
    write_quote(quote, resulting_img_path, text_color, logger)
    write_footer(resulting_img_path, text_color, logger)

    logger.info('quote image created')

    return resulting_img_path


def get_background(background_folder_path):
    backgrounds = [bg for bg in os.listdir(background_folder_path) if bg.endswith(".png")]
    return 'backgrounds/' + random.choice(backgrounds)


def darken_img(img_path, dark_img_path):
    background_img = Image.open(img_path)
    enhancer = ImageEnhance.Brightness(background_img)
    darker_background_img = enhancer.enhance(0.4)
    darker_background_img.save(dark_img_path)


def write_title(today_str, img_path, text_color, logger):
    logger.info('writing title')

    body_font = ImageFont.truetype('fonts/Montserrat-Bold.ttf', 40)

    img = Image.open(img_path)
    draw = ImageDraw.Draw(img)

    title_position = (30, 90)
    draw.text(title_position, today_str, text_color, font=body_font)

    img.save(img_path)


def write_quote(quote, img_path, text_color, logger):
    logger.info('writing quote')

    body_font = ImageFont.truetype('fonts/Montserrat-Regular.ttf', 40)

    img = Image.open(img_path)
    draw = ImageDraw.Draw(img)

    quote_position = (30, 150)
    draw.text(quote_position, quote, text_color, font=body_font)

    img.save(img_path)


def write_footer(img_path, text_color, logger):
    logger.info('writing footer')

    body_font = ImageFont.truetype('fonts/Montserrat-Regular.ttf', 25)

    img = Image.open(img_path)
    draw = ImageDraw.Draw(img)

    quote_position = (400, 620)
    draw.text(quote_position, '@plsinspiremenow', text_color, font=body_font)

    img.save(img_path)
