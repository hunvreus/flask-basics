from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email
from flask_babel import _, lazy_gettext as _l


class LoginForm(FlaskForm):
    email = StringField(_l('Email'), validators=[DataRequired(), Email()])
    submit = SubmitField(_l('Sign in with email'))

    # Validation to limit login to your company.
    # def validate_email(self, email):
    #     if not email.data.endswith('@example.com'):
    #         raise ValidationError(_('This must be an Example.com address.'))