from flask import current_app
from flask import send_file
from model import Post
from model import db
import os


class PostService:
    ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}

    @staticmethod
    def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in PostService.ALLOWED_EXTENSIONS

    @staticmethod
    def create(data, file):
        # print(data, file.filename)
        print(PostService.allowed_file(file))
        with current_app.app_context():
            post = Post(
                user_id=data["user_id"],
                content=data["content"],
                media='/uploads/' + file.filename
            )
            if file.filename == '':
                return None
            if file and PostService.allowed_file(file.filename):
                upload_path = os.path.join(current_app.root_path, "uploads")
                # filename = secure_filename(file.filename)
                file.save(os.path.join(upload_path, file.filename))
                post.filename = file.filename

            db.session.add(post)
            db.session.commit()
            db.session.refresh(post)
            return post

    @staticmethod
    def update(data, id):
        post = Post.query.get(id)
        if post:
            for key, value in data.items():
                if hasattr(post, key):
                    setattr(post, key, value)
            try:
                db.session.commit()
                return True
            except:
                db.session.rollback()
                return False
        else:
            return False

    @staticmethod
    def list():
        posts = Post.query.all()
        post_list = []
        for post in posts:
            post_list.append({
                "id": post.id,
                "username": post.user.username,
                "email": post.user.email,
                "user_id": post.user_id,
                "content": post.content,
                "media": post.media,
                "created_at": post.created_at,
                "updated_at": post.updated_at
            })

        return post_list

    @staticmethod
    def show(id):
        post = Post.query.get(id)
        media_file_path = os.path.join(current_app.root_path, post.media)
        if os.path.isfile(media_file_path):
            return send_file(media_file_path)
        else:
            return post.to_dict()

    @staticmethod
    def delete(id):
        post = Post.query.get(id)
        if post:
            db.session.delete(post)
            db.session.commit()
            return True
        else:
            return False
