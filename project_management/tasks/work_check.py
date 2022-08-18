import os
from datetime import datetime
from celery import Celery
import mongoengine
from project_management.source.config import config_by_name
from project_management.source.models.work import Work
from project_management.tasks.mail_task import send_email

config_name = os.environ.get('PROJECT_ENV', "local")
config_data = config_by_name[config_name]

app = Celery('worker')


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(86400.0, work_planning_control.s(), name='check every day')


@app.task
def work_planning_control(arg):
    mongoengine.connect(host=config_data.MONGODB_URI)
    works = Work.objects()
    for work_object in works:
        planned_start_date = work_object.planned_start_date
        planned_finish_date = work_object.planned_finish_date
        work_state = work_object.state
        if datetime(planned_start_date.year, planned_start_date.month, planned_start_date.day) > datetime.now() \
                and work_state is 1:
            send_email(work_object.mail, "start")
        if datetime(planned_finish_date.year, planned_finish_date.month, planned_finish_date.day) > datetime.now()\
                and work_state is not 4:
            send_email(work_object.mail, "finish")
