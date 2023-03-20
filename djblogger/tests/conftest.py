from pytest_factoryboy import register

from .factories import PostFactory, UserFactory

register(UserFactory)
register(PostFactory)
