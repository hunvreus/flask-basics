from flask_login import UserMixin
from app import db, login
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(320), index=True, unique=True)
    
    def __repr__(self):
        return '<User {}>'.format(self.email)

    @property
    def avatar(self):
        return f'https://unavatar.io/{self.email.lower()}'


@login.user_loader
def load_user(id: int) -> User | None:
    return db.session.get(User, int(id))