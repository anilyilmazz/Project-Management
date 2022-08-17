from flask import request
from flask_restx import Resource, reqparse

from ..util.dto import WorkDto
from ..services.work_service import get_work, get_works, create_work, update_work, delete_work

work_api = WorkDto.api
_work_get_model = WorkDto.get_model
_work_create_model = WorkDto.create_model
_work_update_model = WorkDto.update_model

get_work_parser = reqparse.RequestParser()
get_work_parser.add_argument('project_id', type=str, required=True)


@work_api.route("/")
class WorkData(Resource):
    """
        Work Management
    """
    @work_api.doc('Work List')
    @work_api.marshal_list_with(_work_get_model, envelope='')
    @work_api.expect(get_work_parser)
    def get(self):
        """Present works"""
        project_id = request.args.get('project_id')
        if not project_id:
            work_api.abort(400, description="project_id cannot be empty")
        return get_works(project_id)

    @work_api.expect(_work_create_model, validate=True)
    @work_api.response(201, 'Work successfully created.')
    @work_api.doc('Create a new work')
    def post(self):
        """Create a new work"""
        work_data = request.json
        new_work_id = create_work(work_data)
        return {"id": new_work_id}


@work_api.route('/<work_id>')
@work_api.response(404, 'Work not found.')
class WorkManagement(Resource):
    """
        Work id Management
    """
    @work_api.doc('Get project detail')
    def get(self, work_id):
        """Get a Work"""
        work_object = get_work(work_id)
        if not work_object:
            work_api.abort(404)
        else:
            return work_object.to_json()

    @work_api.expect(_work_update_model, validate=True)
    @work_api.response(204, 'Work successfully updated.')
    @work_api.doc('Update work')
    def put(self, work_id):
        """Update work"""
        work_data = request.json
        updated_work = update_work(work_id, work_data)
        return updated_work.to_json()

    @work_api.doc('Delete work')
    def delete(self, work_id):
        """Delete a Work"""
        deleted_work_id = delete_work(work_id)
        if deleted_work_id:
            return {"id": deleted_work_id}
        else:
            work_api.abort(404)
