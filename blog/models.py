from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.text import slugify
from taggit.managers import TaggableManager


class Post(models.Model):
    choices = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=100, unique=True, validators=[
        MinLengthValidator(3)])
    subtitle = models.CharField(max_length=100, unique=True, validators=[
        MinLengthValidator(3)])
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='post_author')
    content = models.TextField(validators=[MinLengthValidator(5)])
    status = models.CharField(max_length=10, choices=choices, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    tags = TaggableManager()

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
