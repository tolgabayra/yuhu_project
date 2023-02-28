from model import Comment
from model import db


class CommentService:

    @staticmethod
    def create(data):
        comment = Comment(
            user_id=data["user_id"],
            post_id=data["post_id"],
            content=data["content"]
        )
        db.session.add(data)
        db.session.commit()
        db.session.refresh()
        return comment

    @staticmethod
    def update(data, id):
        comment = Comment.query.get(id)
        if comment:
            for key, value in data.items():
                if hasattr(comment, key):
                    setattr(comment, key, value)
            try:
                db.session.commit()
                return True
            except:
                db.session.rollback()
                return False
        else:
            return False

    @staticmethod
    def list_by_post(post_id):
        comments = Comment.query.filter_by(post_id).all()
        comment_list = []
        for comment in comments:
            comment_list.append({
                "id": comment.id,
                "user_id": comment.user_id,
                "post_id": comment.post_id,
                "content": comment.content,
                "created_at": comment.created_at,
                "updated_at": comment.updated_at
            })
        return comment_list


    @staticmethod
    def show(id):
        comment = Comment.query.get(id)
        if comment:
            return {
                "id": comment.id,
                "user_id": comment.user_id,
                "post_id": comment.post_id,
                "content": comment.content
            }
        else:
            return False


    @staticmethod
    def delete(id):
        comment = Comment.query.get(id)
        if comment:
            db.session.delete(id)
            db.session.commit()
            return True
        else:
            return False
