from flask import Blueprint, request
from models.videocard import Videocard, VideocardSchema
from db import db
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

videocard_bp = Blueprint('videocard_bp', __name__)
auth = HTTPBasicAuth()

USER_DATA = {
    "admin": generate_password_hash("admin")
}

@auth.verify_password
def verify(username, password):
    if username in USER_DATA and check_password_hash(USER_DATA.get(username), password):
        return username
    
@videocard_bp.route('/videocards', methods=['GET', 'POST'])
@auth.login_required
def videocards():
    if request.method == 'GET':
        videocards = Videocard.query.all()
        if not videocards:
            return {"message": "No videocards found"}, 404
        return VideocardSchema(many=True).dump(videocards), 200
    if request.method == 'POST':
        new_videocard = Videocard(**request.get_json())
        db.session.add(new_videocard)
        db.session.commit()
        return VideocardSchema().dump(new_videocard), 201

@videocard_bp.route('/videocard/<int:id>', methods=['GET', 'PUT', 'DELETE'])
@auth.login_required
def videocard(int: id):
    videocard = Videocard.query.get(id)
    if videocard is None:
        return {"message": "Videocard not found"}, 404
    if request.method == 'GET':
        return VideocardSchema().dump(videocard), 200
    if request.method == 'PUT':
        data = request.get_json()
        for key, value in data.items():
            setattr(videocard, key, value)
        db.session.commit()
        return VideocardSchema().dump(videocard), 200
    if request.method == 'DELETE':
        db.session.delete(videocard)
        db.session.commit()
        return {"message": "Videocard deleted"}, 204