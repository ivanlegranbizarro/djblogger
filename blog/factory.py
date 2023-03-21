import factory
from django.contrib.auth.models import User

from blog.models import Post


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Faker('sentence', nb_words=4)
    subtitle = factory.Faker('sentence', nb_words=4)
    author = User.objects.get_or_create(username='admin')[0]
    content = factory.Faker('text', max_nb_chars=200)
    status = 'published'
