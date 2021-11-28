import os

from project.models import User
from project.server import create_app, db

app = create_app(os.getenv('FLASK_ENV', 'development'))


@app.shell_context_processor
def shell():
    return {'db': db, 'User': User}
