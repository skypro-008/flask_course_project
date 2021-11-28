import os

from project.server import create_app

app = create_app(os.getenv('FLASK_ENV', 'development'))
