#!/usr/bin/env python3
"""
module: flask app and babel app
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union, Dict

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """class to config babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def basic_app():
    """basic flask app to retrun index"""
    return render_template('6-index.html')


@babel.localeselector
def get_locale():
    """get the default lan from usr"""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user(login_as: int = None) -> Union[Dict, None]:
    """get a user from users fake table"""
    if login_as and int(login_as) in users.keys():
        return users[int(login_as)]
    return None


@app.before_request
def before_request():
    """before request"""
    login_as = request.args.get('login_as')
    user = get_user(login_as)
    g.user = user


if __name__ == '__main__':
    app.run()
