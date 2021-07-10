from pakt_tube import app

from flask import redirect, url_for

from flask_dance.contrib.discord import discord

from pakt_tube.models import db, User

@app.route("/app")
def index():
    if not discord.authorized:
        return redirect(url_for("discord.login"))

    resp = discord.get("/api/users/@me").json()

    if not User.query.filter_by(user_name=resp['username']):

        db.session.add(
            User(
                id=resp['id'],
                user_name=resp['username']
            )
        )

        db.session.commit()

    return dict(User.query.filter_by(user_name=resp['username']))
