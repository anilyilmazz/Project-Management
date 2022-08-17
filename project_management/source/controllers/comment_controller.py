from flask import request
from flask_restx import Resource, reqparse

from ..util.dto import CommentDto
from ..services.comment_service import get_comments, create_comment, update_comment, get_comment, delete_comment

comment_api = CommentDto.api
_comment_get_model = CommentDto.get_model
_comment_create_model = CommentDto.create_model
_comment_update_model = CommentDto.update_model

get_comment_parser = reqparse.RequestParser()
get_comment_parser.add_argument('work_id', type=str, required=True)


@comment_api.route("/")
class ProjectData(Resource):
    """
        Comment Management
    """
    @comment_api.doc('Comment From Works')
    @comment_api.expect(get_comment_parser)
    @comment_api.marshal_list_with(_comment_get_model, envelope='data')
    def get(self):
        """Present comments in Work"""
        work_id = request.args.get('work_id')
        projects = get_comments(work_id)
        return projects

    @comment_api.expect(_comment_create_model, validate=True)
    @comment_api.response(201, 'Comment successfully created.')
    @comment_api.doc('Create a new comment')
    def post(self):
        """Create a new comment"""
        comment_data = request.json
        new_comment_id = create_comment(comment_data)
        return {"id": new_comment_id}


@comment_api.route('/<comment_id>')
@comment_api.response(404, 'Comment not found.')
class CommentManagement(Resource):
    """
        Comment id Management
    """
    @comment_api.doc('Get comment')
    def get(self, comment_id):
        """Get a Comment"""
        comment_object = get_comment(comment_id)
        if not comment_object:
            comment_object.abort(404)
        else:
            return comment_object.to_json()

    @comment_api.expect(_comment_update_model, validate=True)
    @comment_api.response(204, 'Comment successfully updated.')
    @comment_api.doc('Update comment')
    def put(self, comment_id):
        """Update Comment"""
        comment_data = request.json
        updated_comment = update_comment(comment_id, comment_data)
        return updated_comment.to_json()

    @comment_api.doc('Delete work')
    def delete(self, comment_id):
        """Delete a Comment"""
        deleted_comment_id = delete_comment(comment_id)
        if deleted_comment_id:
            return {"id": deleted_comment_id}
        else:
            comment_api.abort(404)
