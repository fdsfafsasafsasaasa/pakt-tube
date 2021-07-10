from flask import Flask

from flask_dance.contrib.discord import make_discord_blueprint
from flask_dance.consumer.storage.sqla import SQLAlchemyStorage

from flask_sqlalchemy import SQLAlchemy

from os import environ

app = Flask(__name__)

app.secret_key = "password"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/pakt_tube.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

blueprint = make_discord_blueprint(
    client_id=environ.get("CLIENT_ID"),
    client_secret=environ.get("CLIENT_SECRET"),
    scope=[
        "identify",
        "email",
    ]
)

from pakt_tube.models import OAuth, db

blueprint.storage = SQLAlchemyStorage(model=OAuth, session=db.session)

app.register_blueprint(blueprint, url_prefix="/login")

import pakt_tube.routes