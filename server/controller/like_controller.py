from flask import Blueprint, json, jsonify, request
from service.like_service import LikeService

like_controller = Blueprint("like_controller", __name__)


@like_controller.route("/", methods=["POST"])
def create_like():
    data = request.get_json()
    like = LikeService.create(data)
    return jsonify({"Message": "Like Created Successfully", "like": like}), 201


# List all like
@like_controller.route("/", methods=["GET"])
def list_like():
    likes = LikeService.list()
    return jsonify({"likes": likes}), 200


# List for post_id

@like_controller.route("/<int:post_id>", methods=["GET"])
def list_like_by_post(post_id):
    likes = LikeService.list_by_post(post_id)
    return jsonify({"likes": likes}), 200


@like_controller.route("/<int:post_id>/<int:user_id>", methods=["DELETE"])
def delete_like(post_id, user_id):
    isOk = LikeService.delete_by_user_id(post_id, user_id)
    if isOk:
        return jsonify({"Message:" "Like deleted Succesfully"}), 200
    else:
        return jsonify({"Message": "Like not found"}), 404
