from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    profile_image = db.Column(db.String(255))
    cover_image = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    posts = db.relationship('Post', backref='user')
    comments = db.relationship('Comment', backref='user')
    followers = db.relationship('Follower', back_populates='user')
    followings = db.relationship('Following', back_populates='user')


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


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    content = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


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
    user = db.relationship('User', back_populates='followings')


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

# User: Kullanıcılar modeli, her kullanıcının birincil anahtarının kullanıcı kimliği (user_id) olduğu bir tablodur.
# Bu model, bir kullanıcının tüm bilgilerini ve birçok ilişkisini içerir. Post: Gönderiler modeli, her gönderinin
# birincil anahtarının gönderi kimliği (post_id) olduğu bir tablodur. Bu model, bir kullanıcının bir gönderisini
# tanımlayan tüm bilgileri ve ilişkileri içerir. Comment: Yorumlar modeli, her yorumun birincil anahtarının yorum
# kimliği (comment_id) olduğu bir tablodur. Bu model, bir kullanıcının bir gönderiye yaptığı yorumu tanımlayan tüm
# bilgileri ve ilişkileri içerir. Like: Beğeniler modeli, her beğeninin birincil anahtarının beğeni kimliği (like_id)
# olduğu bir tablodur. Bu model, bir kullanıcının bir gönderiye veya yoruma yaptığı beğeniye ilişkin tüm bilgileri ve
# ilişkileri içerir. Follower: Takipçiler modeli, her takipçinin birincil anahtarının takipçi kimliği (follower_id)
# olduğu bir tablodur. Bu model, bir kullanıcının diğer kullanıcıları takip etmesini tanımlayan tüm bilgileri ve
# ilişkileri içerir. Following: Takip edilenler modeli, her takip edilenin birincil anahtarının takip edilen kimliği
# (following_id) olduğu bir tablodur. Bu model, bir kullanıcının diğer kullanıcılar tarafından takip edilmesini
# tanımlayan tüm bilgileri ve ilişkileri içerir. Message: Mesajlar modeli, her mesajın birincil anahtarının mesaj
# kimliği (message_id) olduğu bir tablodur. Bu model, bir kullanıcının diğer kullanıcılara gönderdiği mesajları
# tanımlayan tüm bilgileri ve ilişkileri içerir. MessageRecipient: Mesaj alıcıları modeli, her mesaj alıcısının
# birincil anahtarının mesaj alıcısı kimliği (message_recipient_id) olduğu bir tablodur. Bu model, bir mesajın bir
# alıcısını tanımlayan tüm bilgileri ve ilişkileri içerir. Notification: Bildirimler modeli, her bildirimin birincil
# anahtarının bildirim kimliği (notification_id) olduğu bir tablodur. Bu model, bir kullanıcının bir bildirim
# almasını tanımlayan tüm bilgileri ve ilişkileri içerir.
