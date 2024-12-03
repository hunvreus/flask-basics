from flask import render_template
from flask_login import login_required
from app.main import bp
from flask_babel import _


@bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', title=_('Home'))


@bp.route('/about.html')
@login_required
def about():
    return render_template('about.html',  title='About')
