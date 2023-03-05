from flask import Blueprint, jsonify, request, make_response
from service.auth_service import AuthService
from util.helper import Helper
auth_controller = Blueprint("auth_controller", __name__)


@auth_controller.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data["email"]
    password = data["password"]


    data = AuthService.login(email, password)
    if data["access_token"] is None:
        return jsonify({"message": "Invalid email or password"}), 401

    response = jsonify({"access_token": data["access_token"], "user_id": data["user_id"]})
    response.set_cookie('access_token', data["access_token"], httponly=True)
    return response, 200


@auth_controller.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data["username"]
    email = data["email"]
    password = data["password"]

    if not all([username, email, password]):
        return jsonify({'message': 'Missing required parameters'}), 400

    user = AuthService.register(username, email, password)
    return jsonify({'message': 'User registered successfully', 'user': user.to_dict()}), 201


@auth_controller.route("/decode_jwt", methods=["POST"])
def decode_jwt():
    data = request.get_json()
    if not data:
        return jsonify("Error"), 400
    decode_token = Helper.decode_token(data["access_token"])
    if decode_token is None:
        return jsonify("Invalid Token"), 403

    return jsonify({"user_id": decode_token})

