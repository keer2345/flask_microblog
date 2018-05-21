from flask import Blueprint

blueprint = Blueprint('errors', __name__)

if 1 == 1:
    from . import handles
