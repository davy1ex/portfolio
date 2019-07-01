import os


class Config(object):
    DEBUG = True
    LOG_TO_STDOUT = os.environ.get("LOG_TO_STDOUT")