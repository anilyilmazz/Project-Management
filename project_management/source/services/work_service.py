from project_management.source.models.work import Work
from ..util.states import work_states


def get_work(work_id):
    return Work.objects(id=work_id).first()


def get_works(project_id):
    return list(Work.objects(project_id=project_id, is_deleted=False))


def create_work(work):
    new_work = Work(project_id=work["project_id"],
                    title=work["title"],
                    state=work_states["receipt"],
                    content=work["content"],
                    planned_start_date=work["planned_start_date"],
                    planned_finish_date=work["planned_finish_date"],
                    mail=work["mail"])
    new_work.save()
    return str(new_work.id)


def update_work(work_id, work):
    work_object = Work.objects(id=work_id).first()
    if work_object:
        work_object.title = work["title"]
        work_object.state = work["state"]
        work_object.content = work["content"]
        work_object.planned_start_date = work["planned_start_date"]
        work_object.planned_finish_date = work["planned_finish_date"]
        work_object.finish_at = work["finish_at"]
        work_object.mail = work["mail"]
        work_object.save()
    return work_object


def delete_work(work_id):
    work_object = Work.objects(id=work_id).first()
    if work_object:
        work_object.is_deleted = True
        work_object.save()
        return str(work_object.id)
    else:
        return False
