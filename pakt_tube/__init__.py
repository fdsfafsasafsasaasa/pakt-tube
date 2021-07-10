from flask import Flask

from flask_dance.contrib.discord import make_discord_blueprint
from flask_dance.consumer.storage.sqla import SQLAlchemyStorage

from flask_sqlalchemy import SQLAlchemy

from os import environ

app = Flask(__name__)

app.secret_key = "password"

db = SQLAlchemy()

blueprint = make_discord_blueprint(
    client_id=environ.get("CLIENT_ID"),
    client_secret=environ.get("CLIENT_SECRET"),
    scope=[
        "identify",
        "email",
    ]
)

from pakt_tube.models import OAuth, User, db

blueprint.storage = SQLAlchemyStorage(OAuth, db.session, user=User)

app.register_blueprint(blueprint, url_prefix="/login")
