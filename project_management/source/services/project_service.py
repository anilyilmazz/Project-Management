from project_management.source.models.project import Project
from ..util.states import project_states


def get_projects(state):
    if state and state in project_states.keys():
        return list(Project.objects(state=project_states[state]))
    else:
        return list(Project.objects())


def get_project(project_id):
    return Project.objects(id=project_id).first()


def create_project(project):
    new_project = Project(name=project["name"], state=project_states["active"])
    new_project.save()
    return str(new_project.id)


def update_project(project_id, project):
    project_object = Project.objects(id=project_id).first()
    if project_object:
        project_object.name = project["name"]
        project_object.state = project["state"]
        project_object.save()
    return project_object
