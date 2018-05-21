from flask import Blueprint

error = Blueprint('errors', __name__)

if 1 == 1:
    from . import handles
