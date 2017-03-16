# coding: utf-8
from django.core.management.base import BaseCommand

from example.api.models import Post, User

bodies = ['Esse é o primeiro post, aproveite', 'Novo post continue aproveitando']


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = User.objects.all()

        for i, body in enumerate(bodies):
            Post.objects.create(author=users[i % users.count()], title="Título #{}".format(i + 1), body=body)
