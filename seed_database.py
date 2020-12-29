"""Script to seed database."""

import os

import json

from datetime import datetime

import crud

import model

import server


os.system('dropdb youtube_subscribers')

os.system('createdb youtube_subscribers')

model.connect_to_db(server.app)

model.db.create_all()


# Create subscriber table's initial data.

with open('data/subscribers.json') as f:

    subscriber_data = json.loads(f.read())

subscriber_in_db = []

for subscriber in subscriber_data:
    channel_name, month_end_at, subscribers, notes, last_updated= (
                                   subscriber['channel_name'],
                                   subscriber['month_end_at'],
                                   subscriber['subscribers'],
                                   subscriber['notes'],
                                   subscriber['last_updated'])
    db_subscriber = crud.create_subscriber(
                                 channel_name,
                                 month_end_at,
                                 subscribers,
                                 notes,
                                 last_updated)

    subscriber_in_db.append(db_subscriber)
