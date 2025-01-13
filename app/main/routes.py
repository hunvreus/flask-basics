from flask import render_template, flash
from flask_login import login_required
from app.main import bp
from flask_babel import _


@bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', title=_('Home'))


@bp.route('/kitchen-sink.html')
def kitchen_sink():
    flash('This is a regular notification')
    flash('This is an error notification', 'error')
    return render_template('kitchen-sink.html',  title='Kitchen sink')
