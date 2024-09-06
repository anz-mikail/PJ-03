from django.db import models
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField
from django.urls import reverse_lazy


class Post(models.Model):
    TYPE = (
        ('tank', 'Танки'),
        ('heal', 'Хилы'),
        ('dd', 'ДД'),
        ('buyers', 'Торговцы'),
        ('gildemaster', 'Гилдмастеры'),
        ('quest', 'Квестгиверы'),
        ('smith', 'Кузнецы'),
        ('tanner', 'Кожевники'),
        ('potion', 'Зельевары'),
        ('spellmaster', 'Мастер заклинаний'),
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    text = RichTextField()
    category = models.CharField(max_length=20, choices=TYPE, default='tank')


class Response(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
