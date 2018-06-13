from flask.cli import FlaskGroup

from app import create_app, db
from app.models import Message, Notification, Post, User

app = create_app()
cli = FlaskGroup(create_app=create_app)


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Message': Message,
            'Notification': Notification}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
