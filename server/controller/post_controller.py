from flask import Blueprint, request, jsonify
from service.post_service import PostService

post_controller = Blueprint("post_controller", __name__)

# @post_controller.route("/", methods=["POST"])
# def create_post():
#     if 'json' in request.content_type:
#         data = request.get_json()
#     else:
#         data = request.form.to_dict()
#
#     file = request.files.get('file')
#
#     post = PostService.create(data, file)
#     return jsonify({"Message": "Post Created Successfully.", "post": post.to_dict()}), 201


@post_controller.route("/", methods=["POST"])
def create_post():
    data = request.form
    file = request.files['media']
    post = PostService.create(data, file)
    return jsonify({"Message": "Post Created Successfully.", "post": post.to_dict()}), 201


@post_controller.route("/", methods=["GET"])
def list_post():
    posts = PostService.list()
    print(posts)
    return jsonify({"posts": posts}), 200


@post_controller.route("/<int:id>", methods=["GET"])
def show_post(id):
    post = PostService.show(id)
    if post:
        return jsonify(post), 200
    else:
        return jsonify("Post not found"), 404


@post_controller.route("/<int:id>", methods=['DELETE'])
def delete_user(id):
    result = PostService.delete(id)
    if result:
        return jsonify("Post has been deleted."), 200
    else:
        return "Post not found", 404


@post_controller.route("/<int:id>", methods=["PUT"])
def update_user(id):
    result = PostService.update(request.get_json(), id)
    if result:
        return jsonify("Post has been updated."), 200
    else:
        return jsonify("Post not found"), 404
