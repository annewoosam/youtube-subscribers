"""CRUD operations."""

from model import db, Subscriber, connect_to_db

import datetime


def create_subscriber(channel_name, month_end_at, subscribers, notes, last_updated):
   

    subscriber = Subscriber(channel_name=channel_name,
                month_end_at=month_end_at,
                subscribers=subscribers,
                notes=notes,
                last_updated=last_updated)

    db.session.add(subscriber)

    db.session.commit()

    return subscriber

def get_subscribers():
    """Return all rows of subscriber data."""

    return Subscriber.query.all()
 
if __name__ == '__main__':
    from server import app
    connect_to_db(app)
