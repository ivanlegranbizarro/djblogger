import factory
from django.contrib.auth.models import User

from blog.models import Post


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('name')
    email = factory.Faker('email')
    password = factory.Faker('password')
    is_superuser = False
    is_staff = False


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Faker('sentence', nb_words=4)
    subtitle = factory.Faker('sentence', nb_words=4)
    author = factory.SubFactory(UserFactory)
    content = factory.Faker('text', max_nb_chars=200)
    status = 'published'
