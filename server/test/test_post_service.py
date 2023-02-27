from service.post_service import PostService
import tempfile


def test_create_post(test_app, test_db):
    with test_app.app_context():
        post_service = PostService()
        data = {
            "user_id": 9,
            "content": "Test",
        }
        with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as tf:
            tf.write(b"text")
        file = tf.name
        result = post_service.create(data, file)
        assert result.id == 9


def test_list_post(test_app):
    with test_app.app_context():
        post_service = PostService()
        post_list = post_service.list()
        assert len(post_list) == 0



