import os
import logging
import sys

from logging.handlers import RotatingFileHandler


def get_logger():
    try:
        import settings
        logs_folder_path = settings.LOGS_FOLDER_PATH
        app_name = settings.APP_NAME
    except ModuleNotFoundError:
        logs_folder_path = os.getenv('LOGS_FOLDER_PATH')
        app_name = os.getenv('APP_NAME')

    if not os.path.isdir(logs_folder_path):
        os.mkdir(logs_folder_path)
    log_file_path = logs_folder_path + '/' + app_name + '.log'
    if not os.path.isfile(log_file_path):
        log_file = open(log_file_path, "a")
        log_file.close()

    logger = logging.getLogger(app_name)
    logger.setLevel('DEBUG')

    log_format = logging.Formatter("%(asctime)s | %(name)s | %(levelname)s | %(message)s")

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(log_format)
    logger.addHandler(console_handler)

    file_handler = RotatingFileHandler(log_file_path, maxBytes=(1048576 * 5), backupCount=5)
    file_handler.setFormatter(log_format)
    logger.addHandler(file_handler)

    logger.info('logger created')

    return logger
