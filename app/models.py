from flask_login import UserMixin
from app import db, login


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(320), index=True, unique=True)
    
    def __repr__(self):
        return '<User {}>'.format(self.email)

    def avatar(self):
        return f'https://unavatar.io/{self.email.lower()}'


@login.user_loader
def load_user(id):
    return User.query.get(int(id))