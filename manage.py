from app import create_app, db
from flask.cli import FlaskGroup

app = create_app()
cli = FlaskGroup(create_app=create_app)


# @app.shell_context_processor
# def make_shell_context():
#     return {'db': db}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
