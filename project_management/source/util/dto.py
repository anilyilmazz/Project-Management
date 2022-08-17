from flask_restx import Namespace, fields


class MainDto:
    api = Namespace('main', description='Projects Works And Comments')


class ProjectDto:
    api = Namespace('project', description='Project Management')
    get_model = api.model('project', {
        'id': fields.String(description='Project Id'),
        'name': fields.String(required=True, description='Work Name'),
        'state': fields.Integer(required=False, description='Work state', enum=[1, 2], example=1),
        'created_at': fields.Date(required=False, description='Created Date'),
    })
    create_model = api.model('project_create_model', {
        'name': fields.String(required=True, description='Work Name'),
    })
    update_model = api.model('project_update_model', {
        'name': fields.String(required=True, description='Work Name'),
        'state': fields.Integer(required=False, description='Work state', enum=[1, 2], example=1),
    })


class WorkDto:
    api = Namespace('work', description='Work Management')
    get_model = api.model('work', {
        'id': fields.String(description='Work Id'),
        'project_id': fields.String(description='Project Id'),
        'title': fields.String(description='Work Title'),
        'state': fields.Integer(description='Work State', enum=[1, 2, 3, 4], example=1),
        'content': fields.String(description='Work Content'),
        'planned_start_date': fields.Date(description='Work Planned Start Date'),
        'planned_finish_date': fields.Date(description='Work Planned Finish Date'),
        'finish_at': fields.Date(description='Work Finish Date'),
        'mail': fields.String(description='Work User Mail'),
    })
    create_model = api.model('work_create_model', {
        'project_id': fields.String(description='Project Id'),
        'title': fields.String(description='Work Title'),
        'content': fields.String(description='Work Content'),
        'planned_start_date': fields.Date(description='Work Planned Start Date'),
        'planned_finish_date': fields.Date(description='Work Planned Finish Date'),
        'mail': fields.String(description='Work User Mail'),
    })
    update_model = api.model('work_update_model', {
        'title': fields.String(description='Work Title'),
        'state': fields.Integer(description='Work State', enum=[1, 2, 3, 4], example=1),
        'content': fields.String(description='Work Content'),
        'planned_start_date': fields.Date(description='Work Planned Start Date'),
        'planned_finish_date': fields.Date(description='Work Planned Finish Date'),
        'finish_at': fields.Date(description='Work Finish Date'),
        'mail': fields.String(description='Work User Mail'),
    })


class CommentDto:
    api = Namespace('comment', description='Comment Management')
    get_model = api.model('comment', {
        'comment': fields.String(required=True, description='Comment'),
        'created_at': fields.Date(required=False, description='Created Date'),
    })
    create_model = api.model('comment_create_model', {
        'work_id': fields.String(required=True, description='Work Id'),
        'comment': fields.String(required=True, description='Comment'),
    })
    update_model = api.model('comment_update_model', {
        'comment': fields.String(required=True, description='Comment'),
    })
