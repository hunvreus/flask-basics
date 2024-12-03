import os
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'), override=True)


class Config(object):
    LANGUAGES = ['en']
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'random-unique-secret-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    APP_NAME = os.environ.get('APP_NAME')
    APP_DESCRIPTION = os.environ.get('APP_DESCRIPTION')
    APP_SOCIAL_IMAGE = os.environ.get('APP_SOCIAL_IMAGE')
    TEMPLATES_AUTO_RELOAD = os.environ.get('TEMPLATES_AUTO_RELOAD') or False
    RESEND_API_KEY = os.environ.get('RESEND_API_KEY')