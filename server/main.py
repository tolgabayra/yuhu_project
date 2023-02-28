from flask import Flask
from flask_cors import CORS
from controller.auth_controller import auth_controller
from controller.post_controller import post_controller
from controller.like_controller import like_controller
from config import Config
from model import db


def create_app(config_class=Config):
    app = Flask(__name__, static_folder="uploads")
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:root@localhost/postgres'
    app.config.from_object(config_class)
    app.config['UPLOAD_FOLDER'] = 'uploads'
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

    db.init_app(app)
    with app.app_context():
        db.create_all()
    # cors
    CORS(app)
    app.register_blueprint(auth_controller, url_prefix="/api/v1/auth")
    app.register_blueprint(like_controller, url_prefix="/api/v1/likes")
    app.register_blueprint(post_controller, url_prefix="/api/v1/posts")

    return app


# kod bloğu, bir Python dosyasının başka bir dosya tarafından modül olarak kullanılmayıp, doğrudan çalıştırılması
# durumunda yürütülecek kodları içeren bir yapıdır.
if __name__ == '__main__':
    my_app = create_app()
    my_app.run(port=5000)
