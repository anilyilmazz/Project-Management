import os

from project_management.source import create_app
from project_management import blueprint

project_environment = os.environ.get('PROJECT_ENV', "local")
app = create_app(project_environment)
app.register_blueprint(blueprint)

app.app_context().push()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
