from werkzeug.security import generate_password_hash, check_password_hash
from .models import *
from flask import request, jsonify, Blueprint
from flask_jwt_extended import create_refresh_token, get_jwt_identity, jwt_required, verify_jwt_in_request

token = Blueprint('token', __name__)
token_id = ''


def refresh_token_get(username):
    refresh_token = create_refresh_token(identity=username)
    global token_id
    token_id = refresh_token
    return refresh_token


@token.route('/refresh_token/<toke>', methods=['GET'])
@jwt_required(refresh=True)
def refresh_token(toke):
    global token_id
    token_id = toke
    email = get_jwt_identity()
    print(email)
    user = User.query.filter_by(email=email).first()
    if user:
        return ("<input type = button value = 後退 onclick =\"window.history.back()\">")
    return 'Flase'


@token.route('/get_token/<toke>', methods=['GET'])
def get_token(toke):
    sum = 'sdfkjeiqwijdij38489feiwj3r89udvjis4htih8vys804hdsh8y8ehw3r893987544651454+46565-8487215ekhgeuihouoawuhdhahoiwhd9pwhegqhwdnjsklallq'
    if 'token_id' in globals():
        if toke == sum:
            return token_id
    return 'Flase'
