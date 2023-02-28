from flask import Blueprint, jsonify, request
from service.comment_service import CommentService

comment_controller = Blueprint("comment_controller", __name__)


@comment_controller.route("/", methods=["POST"])
def create_comment():
    data = request.get_json()
    comment = CommentService.create(data)
    return jsonify({"Message: ": "Comment Created Successfully.", "comment: ": comment.to_dict()}), 201


@comment_controller.route("/<int:post_id>", methods=["GET"])
def list_comments(post_id):
    comments = CommentService.list_by_post(post_id)
    return jsonify({"comments": comments})


@comment_controller.route("/<int:id>", methods=["GET"])
def show_comment(id):
    comment = CommentService.show(id)
    if comment:
        return jsonify(comment), 200
    else:
        return jsonify("Comment not found"), 404


@comment_controller.route("/<int:id>", methods=["DELETE"])
def delete_comment(id):
    result = CommentService.delete(id)
    if result:
        return jsonify("Comment has been deleted"), 200
    else:
        return jsonify("Post is not found"), 404



@comment_controller.route("/<int:id>", methods=["PUT"])
def update_comment(id):
    result = CommentService.update(request.get_json(), id)
    if result:
        return jsonify("Comment has been updated"), 200
    else:
        return jsonify("Comment not found"), 404


