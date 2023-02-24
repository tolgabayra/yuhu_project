from flask import Blueprint, request, jsonify, make_response
from service.post_service import PostService

post_controller = Blueprint("post_controller", __name__)


@post_controller.route("/", methods=["POST"])
def create_post():
    data = request.get_json()
    post = PostService.create(data)
    return jsonify(post), 201


@post_controller.route("/", methods=["GET"])
def list_post():
    posts = PostService.list()
    return jsonify(posts), 200


@post_controller.route("/<int:id>", methods=["GET"])
def show_post(id):
    post = PostService.show(id)
    if post:
        return jsonify(post), 200
    else:
        return jsonify("user not found"), 404


@post_controller.route("/<int:id>/", methods=['DELETE'])
def delete_user(id):
    result = PostService.delete(id)
    if result:
        return jsonify("Post has been delted."), 200
    else:
        return "Post not found", 404


@post_controller.route("/<int:id>", methods=["PUT"])
def update_user(id):
    result = PostService.update(id, request.get_json())
    if result:
        return jsonify("Post has been updated."), 200
    else:
        return jsonify("Post not found"), 404
