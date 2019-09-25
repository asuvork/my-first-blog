from __future__ import absolute_import, unicode_literals
from celery import shared_task

from blog.models import Post
from django.contrib.auth.models import User

@shared_task
def addPost():
    me = User.objects.get(username='admin')
    Post.objects.create(author=me, title='Sample title Celery', text='Celery')


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)
