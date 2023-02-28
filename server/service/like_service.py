from datetime import datetime
from model import Like
from model import db
import os

class LikeService:

    @staticmethod
    def create(data):
        like = Like(
            user_id=data["user_id"],
            post_id=data["post_id"],
            comment_id=["comment_id"]
        )
        db.session.add(like)
        db.session.commit()
        db.session.refresh(like)
        return like

    @staticmethod
    def update(data, id):
        like = Like.query.get(id)
        if like:
            for key, value in data.items():
                if hasattr(like, key):
                    setattr(like, key, value)
            like.updated_at = datetime.utcnow()
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
        likes = Like.query.all()
        like_list = []
        for like in likes:
            like_list.append({
                "id": like.id,
                "user_id": like.user_id,
                "content": like.post_id,
                "media": like.comment_id,
                "created_at": like.created_at,
                "updated_at": like.updated_at
            })

        return like_list


    @staticmethod
    def show(id):
        like = Like.query.get(id)
        if like:
            return {
                "id": like.id,
                "user_id": like.user_id,
                "post_id": like.post_id,
                "comment_id": like.comment_id
            }
        else:
            return False

    @staticmethod
    def delete(id):
        like = Like.query.get(id)
        if like:
            db.session.delete(like)
            db.session.commit()
            return True
        else:
            return False



    @staticmethod
    def list_by_post(post_id):
        likes = Like.query.filter_by(post_id).all()
        like_list = []
        for like in likes:
            like_list.append({
                "id": like.id,
                "user_id": like.user_id,
                "content": like.post_id,
                "media": like.comment_id,
                "created_at": like.created_at,
                "updated_at": like.updated_at
            })
        return like_list

    @staticmethod
    def delete_by_user_id(post_id, user_id):
        like = Like.query.filter_by(post_id, user_id).first()
        if like:
            db.session.delete(like)
            db.session.commit()
            return True
        else:
            return False





















