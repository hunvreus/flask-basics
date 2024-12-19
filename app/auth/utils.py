from flask import render_template, current_app
from flask_babel import _
from app.email import send_email
from time import time
import jwt


def send_login_email(email):
    token = get_login_token(email)
    send_email(
        _('Sign in to %(app_name)s', app_name=current_app.config['APP_NAME']),
        sender=(
            current_app.config['MAIL_SENDER_NAME'],
            current_app.config['MAIL_SENDER_EMAIL']
        ),
        recipients=[email],
        text_body=render_template(
            'email/login.txt',
            app_logo=current_app.config['APP_LOGO'],
            app_name=current_app.config['APP_NAME'],
            email=email,
            token=token,
            footer=current_app.config['MAIL_FOOTER']
        ),
        html_body=render_template(
            'email/login.html',
            app_name=current_app.config['APP_NAME'],
            email=email,
            token=token,
            footer=current_app.config['MAIL_FOOTER']
        )
    )


def get_login_token(email, expires_in=600):
        return jwt.encode(
            {'login': email, 'exp': time() + expires_in},
            current_app.config['SECRET_KEY'],
            algorithm='HS256'
        )


def verify_login_token(token):
    try:
        email = jwt.decode(
            token,
            current_app.config['SECRET_KEY'],
            algorithms=['HS256']
        )['login']
    except:
        return
    return email