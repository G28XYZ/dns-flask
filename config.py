import os

class Config(object):
    SECRET_KEY = str(os.environ.get('SECRET_KEY')) or 'you-will-never-guess'
    DEBUG = True
    