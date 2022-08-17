import json
from bson import json_util
from ..services.main_service import get_project_works_comments
from flask_restx import Resource
from ..util.dto import MainDto

main_api = MainDto.api


@main_api.route("/")
class MainData(Resource):
    """
        Project Management
    """
    @main_api.doc('Projects, Works and Comments')
    def get(self):
        """Present projects, works, comments"""
        present_project_data = get_project_works_comments()
        return json.loads(json_util.dumps(present_project_data))
