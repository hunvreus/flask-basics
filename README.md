This is a simple and opiniated boilerplate for Flask apps (mostly ripped off from [Miguel Grinberg's awesome Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)).

# Main features

- Code organized in [Blueprints](https://flask.palletsprojects.com/en/stable/blueprints/)
- i18n support with [Flask-Babel](https://python-babel.github.io/flask-babel/)
- Forms with [Flask-WTForms](https://flask-wtf.readthedocs.io/en/1.2.x/)
- Database ORM with SQLAlchemy (defaults to SQLite).
- Email with [Resend](https://resend.com) and email templates with [MJML](https://mjml.io/).
- CSS with [Tailwind CSS](https://tailwindcss.com/).
- Javascript with [Alpine.js](https://alpinejs.dev/) and (optionally) [HTMX](https://htmx.org/).

# Prerequisites

- Python 3.
- Node.js/npm for developement (CSS, email template, favicons, ...).

# Install & Run

1. **[Make a copy of this template](https://github.com/hunvreus/flask-basics/generate)** and `git clone` the repository you created.
2. Create your virtual environment and activate it:
    ```
    python3 -m venv venv
    source venv/bin/activate
    ```
3. Install the dependencies:
    ```
    pip install -r requirements.txt 
    ```
4. Initiate your database migrations and create the tables:
    ```
    flask db migrate # This will create a "migrations/" folder
    flask db upgrade # This may create an "app.db" file
    ```
5. Create your local environment configuration file:
    ```
    cp .env.example .env
    ```
6. Start the app:
    ```
    flask run
    ```

# Environment variables

Variable | Default | Description
--- | --- | ---
`APP_NAME` | `"App name"` | The name of the app displayed in the header, emails, user messagse, etc.
`APP_DESCRIPTION` | `None` | The default `<meta>` description, can be overriden for any route by defining the description template variable.
`APP_SOCIAL_IMAGE` | `'/social.png'` | The image used for social cards.
`MAIL_SENDER_NAME` | `APP_NAME` | The name used when sending emails.
`MAIL_SENDER_EMAIL` | `'noreply@example.com'` | The email used when sending emails.
`MAIL_LOGO` | `'/assets/logo/logo-72x72.png'` | Logo used in the HTML email template (see `app/templates/email/login.html`).
`MAIL_FOOTER` | `None` | A text to be included in the footer of your emails (e.g. your business address).
`SECRET_KEY` | `'random-unique-secret-key'` | [Secret key used for signing session cookies](https://flask.palletsprojects.com/en/stable/config/#SECRET_KEY).
`SQLALCHEMY_DATABASE_URI` | `None` | [A valid database connection URI](https://flask-sqlalchemy.readthedocs.io/en/stable/config/#flask_sqlalchemy.config.SQLALCHEMY_DATABASE_URI). If undefined, the app will use an SQLite database saved at `app.db`.
`RESEND_API_KEY` | `None` | The [Resend](https://resend.com) API key. If no key is provided (e.g. when developing on local), the content of the emails sent will be displayed in your terminal.
`TEMPLATES_AUTO_RELOAD` | `False` | [Hot reload templates](https://flask.palletsprojects.com/en/stable/config/#TEMPLATES_AUTO_RELOAD) when they change (for development).

# Models

Models are defined in `/app/models.py`. After making any change you will need to:

1. Create the migration script:
    ```
    flask db migrate -m "users table"
    ```
2. Run the migration:
    ```
    flask db upgrade #undo with "downgrade"
    ```

# i18n

To create translations of your app strings:

1. Generate the `.pot` file:
    ```
    pybabel extract -F babel.cfg -k _l -o messages.pot .
    ```
2. Generate a language catalog for a language (in this example Spanish with `es`):
    ```
    pybabel init -i messages.pot -d app/translations -l es
    ```
3. Once you've added your translations in the language catalog generated in the previous step, you can compile translations to be used by Flask:
    ```
    pybabel compile -d app/translations
    ```

You'll need to add the support for additional languages in the `LANGUAGES` array in '`config.py`.

Later on, if you need ot update translations you can run: 

```
pybabel extract -F babel.cfg -k _l -o messages.pot .
pybabel update -i messages.pot -d app/translations
```

# Assets (CSS, images, email template)

*To run any of the npm commands listed below, you need to install the dev depdendencies with `npm install`.*

- **CSS**: You can modify the `/app/src/main.css` file and run the build process with `npm run css:build`, or `npm run css:dev` if you want to watch changes.
- **Favicon**: These files are saved in `app/static/favicon/`. You can generate these files by editing the `src/favicon.svg` file and then running `npm run favicon`.
- **Social cards** (OG and Twitter/X): These files are saved in `app/static/social/`. You can generate these files by editing the `src/social.svg` file and then running `npm run social`.
- **Logo**: The logo is saved in both SVG and PNG formats at multiple resolutions in `app/static/logo`. You can generate these files by editing the `src/logo.svg` file and then running `npm run logo`.
- **Email template**: The login email templates (HTML and text) are saved in `app/templates/email/`. The HTML version can be generated from the [MJML](https://mjml.io/) template defined at `src/login.mjml` by running the `npm run email` command.

You can generate all assets at once by running the `npm run build` command.


ok
