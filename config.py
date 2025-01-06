import os
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'), override=True)


class Config(object):
    APP_NAME = os.environ.get('APP_NAME') or 'App name'
    APP_DESCRIPTION = os.environ.get('APP_DESCRIPTION') or 'App description'
    APP_SOCIAL_IMAGE = os.environ.get('APP_SOCIAL_IMAGE') or '/social.png'
    LANGUAGES = ['en']
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'random-unique-secret-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SENDER_NAME = os.environ.get('MAIL_SENDER_NAME') or APP_NAME
    MAIL_SENDER_EMAIL = os.environ.get('MAIL_SENDER_EMAIL') or 'noreply@example.com'
    MAIL_LOGO = os.environ.get('MAIL_LOGO') or '/favicon-96x96.png'
    MAIL_FOOTER = os.environ.get('MAIL_FOOTER')
    RESEND_API_KEY = os.environ.get('RESEND_API_KEY')
    TEMPLATES_AUTO_RELOAD = os.environ.get('TEMPLATES_AUTO_RELOAD') or False