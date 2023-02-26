from model import Post
from model import db


class PostService:

    @staticmethod
    def create(data):
        print(data)
        print("---------------------SERVICE----------------")
        post = Post(
            user_id=data["user_id"],
            content=data["content"]
        )
        db.session.add(post)
        db.session.commit()
        print("-------------BAŞARILI--------------------")
        print("-------------BAŞARILI--------------------")
        print("-------------BAŞARILI--------------------")
        print("-------------BAŞARILI--------------------")
        print("-------------BAŞARILI--------------------")
        print("-------------BAŞARILI--------------------")

        return post

    @staticmethod
    def update(data, id):
        post = Post.query.get(id)
        if post:
            for key, value in data.items():
                setattr(post, key, value)
                db.session.commit()
                return True
        else:
            return False

    @staticmethod
    def list():
        return Post.query.all()

    @staticmethod
    def show(id):
        return Post.query.get(id)

    @staticmethod
    def delete(id):
        post = Post.query.get(id)
        if post:
            db.session.delete(post)
            db.session.commit()
            return True
        else:
            return False
