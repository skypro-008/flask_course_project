import os

from project.models import Director, Genre, Movie, User
from project.server import create_app, db

app = create_app(os.getenv('FLASK_ENV', 'development'))


@app.shell_context_processor
def shell():
    return {'db': db, 'User': User, 'Director': Director, 'Genre': Genre, 'Movie': Movie}
