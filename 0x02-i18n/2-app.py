#!/usr/bin/env python3
"""
module: flask app and babel app
"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """class to config babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def basic_app():
    """basic flask app to retrun index"""
    return render_template('1-index.html')


@babel.localeselector
def get_locale():
    """get the default lan from usr"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run()
