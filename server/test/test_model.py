from model import Post


class TestModel:
    def test_new_post(self):
        post = Post(1, "content_writer", "media_writer")

        assert post.content == "content_writer"
        assert post.media == "media_writer"
