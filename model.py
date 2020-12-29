from flask_sqlalchemy import SQLAlchemy

import datetime

db = SQLAlchemy()

class Subscriber(db.Model):
    """A class for subscribers."""
    
    __tablename__ = 'subscribers'

    subscriber_id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    channel_name = db.Column(db.String)

    month_end_at = db.Column(db.Date)

    subscribers = db.Column(db.Integer)

    notes = db.Column(db.String)

    last_updated = db.Column(db.Date)

    def __repr__(self):
        return f'<Subscriber subscriber_id={self.subscriber_id} channel_id={self.channel_id}>'

def connect_to_db(flask_app, db_uri='postgresql:///youtube_subscribers', echo=True):
   
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
   
    flask_app.config['SQLALCHEMY_ECHO'] = echo
   
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    
    db.init_app(flask_app)

    print('Connected to the db!')

if __name__ == '__main__':

    from server import app

    connect_to_db(app)