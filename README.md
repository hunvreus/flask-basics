This is a simple starter project for Flask apps (mostly ripped off from [Miguel Grinberg's awesome Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)).

# Prerequisites

- Python 3
- Node.js and npm (if you plan on changing the CSS)

# Install & Run

1. Clone this repository and cd to the root in your terminal.
2. Create your virtual environment and activate it:
    ```
    python3 -m venv venv
    source venv/bin/activate
    ```
3. Install the dependencies:
    ```
    pip install -r requirements.txt 
    ```
4. Create the tables (this will create an `app.db` SQLite file):
    ```
    flask db upgrade
    ```
5. Create your local environment configuration file:
    ```
    cp .env.example .env
    ```
6. Start the app:
    ```
    flask run
    ```
7. Start your local emulated email server (in another terminal window/tab):
    ```
    python3 -m smtpd -n -c DebuggingServer localhost:8025
    ```

# Configure email

The `.env.example` file you copied contains settings for the mail server:

```
MAIL_SERVER = localhost
MAIL_PORT = 8025
```

This works for running a local emulated email server for development.

You can send real emails by commenting these two lines and uncommenting all of the lines above. You'll need to adjust the settings (the example assumes you'll use Sendgrid).

# Modify CSS

You will need to install [Tailwind CSS](https://tailwindcss.com/) and depdenceies by running `npm install`. You can modify the `/app/src/main.css` file and run the build process with the following command:

```
npx tailwindcss -i ./app/src/main.css -o ./app/static/main.css --watch
```

# Modify tables

Models are defined in the `/app/models.py` file. After making any change you will need to:

1. Create the migration script:
    ```
    flask db migrate -m "users table"
    ```
2. Run the migration:
    ```
    flask db upgrade #undo with "downgrade"
    ```

# Translation

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

# Todos

- [ ] Create a better template for transactional emails
- [ ] Add deployment instructions