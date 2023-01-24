from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, g, current_app
from flask_login import current_user, login_required
from flask_babel import _, get_locale
from app import db
from app.main.forms import UserForm, PostForm
from app.models import User, Post
from app.main import bp
from werkzeug.urls import url_parse

@bp.before_app_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()
    g.locale = str(get_locale())


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/posts', methods=['GET', 'POST'])
@login_required
def index():
    page = request.args.get("page", 1, type=int)
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(page=page, per_page=current_app.config['POSTS_PER_PAGE'], error_out=False)
    return render_template('posts/list.html', title=_('Home'), posts=posts, endpoint='main.index')


@bp.route('/posts/new', methods=['GET', 'POST'])
@login_required
def post_add():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(
            title=form.title.data,
            body=form.body.data,
            author=current_user
        )
        db.session.add(post)
        db.session.commit()
        flash(_('Your post is now live!'))
        return redirect(url_for('main.index'))
    return render_template('posts/add.html', title=_('Add a post'), form=form)


@bp.route('/posts/<int:id>')
@login_required
def post_view(id):
    post = Post.query.filter_by(id=id).first_or_404()
    return render_template('posts/view.html', title=post.title, post=post)


@bp.route('/posts/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def post_edit(id):
    post = Post.query.filter_by(id=id).first_or_404()
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.body = form.body.data
        post.author = current_user
        db.session.commit()
        flash(_('Your changes have been saved.'))
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main.post_view', id=id)
        return redirect(next_page)
    elif request.method == 'GET':
        form.title.data = post.title
        form.body.data = post.body
    return render_template('posts/edit.html', title=_('Add a post'), form=form)


@bp.route('/users/<int:id>')
@login_required
def user_view(id):
    user = User.query.filter_by(id=id).first_or_404()
    return render_template('users/view.html', user=user)


@bp.route('/users/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def user_edit(id):
    # TODO: add check for permission to edit profile
    form = UserForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash(_('Your changes have been saved.'))
        return redirect(url_for('main.user_view', id=id))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    return render_template('users/edit.html', title=_('Edit Profile'), form=form)


@bp.route('/about')
@login_required
def about():
    return render_template('about.html',  title=_('About'))
