from pakt_tube import app

from flask import redirect, url_for

from flask_dance.contrib.discord import discord

@app.route("/")
def index():
    if not discord.authorized:
        return redirect(url_for("discord.login"))
    resp = discord.get("/api/users/@me")

    return resp.json()