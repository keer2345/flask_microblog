from flask import Blueprint

blueprint = Blueprint('main', __name__)

if 1 == 1:
    from app.main import routes
