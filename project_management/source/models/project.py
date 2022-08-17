from mongoengine import Document, StringField, DateTimeField, IntField
import datetime


class Project(Document):
    name = StringField(required=True)
    state = IntField(min_value=1, max_value=2)
    created_at = DateTimeField(default=datetime.datetime.utcnow)

