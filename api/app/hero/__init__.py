from flask import Blueprint

bp = Blueprint('hero', __name__)

from app.hero import routes
