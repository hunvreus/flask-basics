from flask import render_template, redirect, url_for, flash, request
from urllib.parse import urlparse
from flask_login import login_user, logout_user, current_user
from app import db
from sqlalchemy import select
from app.auth import bp
from app.auth.forms import LoginForm
from app.models import User
from app.auth.utils import send_login_email, verify_login_token
from flask_babel import _


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        send_login_email(form.email.data)
        flash(_("We've sent you an email with a link to log in."))
        return redirect(url_for('main.index'))
    return render_template('auth/login.html', title=_('Log in'), form=form)


@bp.route('/login/<token>', methods=['GET', 'POST'])
def login_with_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    email = verify_login_token(token)
    if email is None:
        flash(_('Invalid token.'))
        return redirect(url_for('main.index'))
    else:
        user = db.session.scalar(
            select(User).where(User.email == email).limit(1)
        )
        if user is None:
            user = User(email=email)
            db.session.add(user)
            db.session.commit()
            flash(_('Congratulations, you are now a registered user.'))
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or urlparse(next_page).netloc != '':
            next_page = url_for('main.index')
        return redirect(next_page)