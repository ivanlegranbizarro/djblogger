import pytest
from django.utils.text import slugify

pytestmark = pytest.mark.django_db


class TestPostModel:
    def test_str_return(self, post_factory):
        post = post_factory()
        assert post.__str__() == post.title

    def test_save_method(self, post_factory):
        post = post_factory()
        assert post.slug == slugify(post.title)
