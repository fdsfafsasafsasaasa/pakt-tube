from flask_dance.consumer.storage.sqla import OAuthConsumerMixin

from pakt_tube import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String)

class OAuth(OAuthConsumerMixin, db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    user = db.relationship(User)

class Channel(User):
    id = db.Column(db.Integer, db.ForeignKey(User.id), primary_key=True)
    channel_name = db.Column(db.String)

    __mapper_args__ = {
        'polymorphic_identity': 'channel',
    }
