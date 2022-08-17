from flask_restx import Resource, reqparse
from flask import request
from ..util.dto import ProjectDto
from ..services.project_service import get_projects, create_project, update_project, get_project

project_api = ProjectDto.api
_project_get_model = ProjectDto.get_model
_project_create_model = ProjectDto.create_model
_project_update_model = ProjectDto.update_model

get_list_parser = reqparse.RequestParser()
get_list_parser.add_argument('state', type=str, required=True, choices=("active", "archive"))


@project_api.route("/")
class ProjectData(Resource):
    """
        Project Management
    """
    @project_api.doc('Project List')
    @project_api.marshal_list_with(_project_get_model, envelope='')
    @project_api.expect(get_list_parser)
    def get(self):
        """Present projects"""
        state = request.args.get('state')
        projects = get_projects(state)
        return projects

    @project_api.expect(_project_create_model, validate=True)
    @project_api.response(201, 'Project successfully created.')
    @project_api.doc('Create a new project')
    def post(self):
        """Create a new project"""
        project_data = request.json
        new_project_id = create_project(project_data)
        return {"id": new_project_id}


@project_api.route('/<project_id>')
@project_api.param('id', 'Project id')
@project_api.response(404, 'Project not found.')
class ProjectView(Resource):
    """
        Project id Management
    """
    @project_api.doc('Get project detail')
    def get(self, project_id):
        """Get a project"""
        project_object = get_project(project_id)
        if not project_object:
            project_api.abort(404)
        else:
            return project_object.to_json()

    @project_api.expect(_project_update_model, validate=True)
    @project_api.response(204, 'Project successfully updated.')
    @project_api.doc('Update project')
    def put(self, project_id):
        """Update project"""
        project_data = request.json
        updated_project = update_project(project_id, project_data)
        return updated_project.to_json()
