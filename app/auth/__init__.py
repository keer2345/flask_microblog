from flask import Blueprint

blueprint = Blueprint('auth', __name__)

if 1 == 1:
    from . import routes
