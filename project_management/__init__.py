from flask_restx import Api
from flask import Blueprint

from .source.controllers.main_controller import main_api as main_ns
from .source.controllers.project_controller import project_api as project_ns
from .source.controllers.work_controller import work_api as work_ns
from .source.controllers.comment_controller import comment_api as comment_ns

blueprint = Blueprint('api', __name__)
api = Api(
    blueprint,
    title='Project Management',
    version='1.0',
    description='Project Management app with flask',
    doc='/doc'
)

api.add_namespace(main_ns, path="/")
api.add_namespace(project_ns, path="/project")
api.add_namespace(work_ns, path="/work")
api.add_namespace(comment_ns, path="/comment")
