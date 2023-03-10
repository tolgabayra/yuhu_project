from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import check_password_hash

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(255), nullable=True)
    last_name = db.Column(db.String(255), nullable=True)
    profile_image = db.Column(db.String(255))
    cover_image = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    posts = db.relationship('Post', backref='user')
    comments = db.relationship('Comment', backref='user')
    followers = db.relationship('Follower', back_populates='user')
    followings = db.relationship('Following', back_populates='user', foreign_keys='Following.follower_id')

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    content = db.Column(db.String(255), nullable=False)
    media = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    comments = db.relationship('Comment', backref='post')
    likes = db.relationship('Like', backref='post')

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'content': self.content,
            'media': self.media,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    content = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'post_id': self.post_id,
            'content': self.content,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }


class Like(db.Model):
    __tablename__ = 'likes'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    comment_id = db.Column(db.Integer, db.ForeignKey('comments.id'))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


class Follower(db.Model):
    __tablename__ = 'followers'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user = db.relationship('User', back_populates='followers')


class Following(db.Model):
    __tablename__ = 'followings'
    id = db.Column(db.Integer, primary_key=True)
    follower_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user = db.relationship('User', back_populates='followings', foreign_keys='Following.user_id')

class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    content = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    recipients = db.relationship('MessageRecipient', backref='message')


class MessageRecipient(db.Model):
    __tablename__ = 'message_recipients'
    id = db.Column(db.Integer, primary_key=True)
    message_id = db.Column(db.Integer, db.ForeignKey('messages.id'))
    recipient_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


class Notification(db.Model):
    __tablename__ = 'notifications'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    message = db.Column(db.String(255), nullable=False)
    read = db.Column(db.Integer, nullable=False, default=0)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# User: Kullan??c??lar modeli, her kullan??c??n??n birincil anahtar??n??n kullan??c?? kimli??i (user_id) oldu??u bir tablodur.
# Bu model, bir kullan??c??n??n t??m bilgilerini ve bir??ok ili??kisini i??erir. Post: G??nderiler modeli, her g??nderinin
# birincil anahtar??n??n g??nderi kimli??i (post_id) oldu??u bir tablodur. Bu model, bir kullan??c??n??n bir g??nderisini
# tan??mlayan t??m bilgileri ve ili??kileri i??erir. Comment: Yorumlar modeli, her yorumun birincil anahtar??n??n yorum
# kimli??i (comment_id) oldu??u bir tablodur. Bu model, bir kullan??c??n??n bir g??nderiye yapt?????? yorumu tan??mlayan t??m
# bilgileri ve ili??kileri i??erir. Like: Be??eniler modeli, her be??eninin birincil anahtar??n??n be??eni kimli??i (like_id)
# oldu??u bir tablodur. Bu model, bir kullan??c??n??n bir g??nderiye veya yoruma yapt?????? be??eniye ili??kin t??m bilgileri ve
# ili??kileri i??erir. Follower: Takip??iler modeli, her takip??inin birincil anahtar??n??n takip??i kimli??i (follower_id)
# oldu??u bir tablodur. Bu model, bir kullan??c??n??n di??er kullan??c??lar?? takip etmesini tan??mlayan t??m bilgileri ve
# ili??kileri i??erir. Following: Takip edilenler modeli, her takip edilenin birincil anahtar??n??n takip edilen kimli??i
# (following_id) oldu??u bir tablodur. Bu model, bir kullan??c??n??n di??er kullan??c??lar taraf??ndan takip edilmesini
# tan??mlayan t??m bilgileri ve ili??kileri i??erir. Message: Mesajlar modeli, her mesaj??n birincil anahtar??n??n mesaj
# kimli??i (message_id) oldu??u bir tablodur. Bu model, bir kullan??c??n??n di??er kullan??c??lara g??nderdi??i mesajlar??
# tan??mlayan t??m bilgileri ve ili??kileri i??erir. MessageRecipient: Mesaj al??c??lar?? modeli, her mesaj al??c??s??n??n
# birincil anahtar??n??n mesaj al??c??s?? kimli??i (message_recipient_id) oldu??u bir tablodur. Bu model, bir mesaj??n bir
# al??c??s??n?? tan??mlayan t??m bilgileri ve ili??kileri i??erir. Notification: Bildirimler modeli, her bildirimin birincil
# anahtar??n??n bildirim kimli??i (notification_id) oldu??u bir tablodur. Bu model, bir kullan??c??n??n bir bildirim
# almas??n?? tan??mlayan t??m bilgileri ve ili??kileri i??erir.


