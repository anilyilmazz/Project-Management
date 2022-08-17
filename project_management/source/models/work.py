from mongoengine import Document, StringField, DateTimeField, IntField, ObjectIdField, BooleanField
import datetime


class Work(Document):
    project_id = ObjectIdField()
    title = StringField(required=True)
    state = IntField(min_value=1, max_value=4)
    content = StringField(required=True)
    planned_start_date = DateTimeField()
    planned_finish_date = DateTimeField()
    created_at = DateTimeField(default=datetime.datetime.utcnow)
    finish_at = DateTimeField()
    mail = StringField(required=False)
    is_deleted = BooleanField(default=False)
