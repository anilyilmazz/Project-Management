from mongoengine import Document, StringField, DateTimeField, ObjectIdField
import datetime


class Comment(Document):
    work_id = ObjectIdField()
    comment = StringField(required=True)
    created_at = DateTimeField(default=datetime.datetime.utcnow)
