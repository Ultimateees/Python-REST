from flask import Blueprint, request

# index page
index_bp = Blueprint('index_bp', __name__)


@index_bp.route('/', methods=['GET'])
def index():
    return {"message": "Welcome to Videocards API, navigate to /videocards to see all videocards"}, 200
