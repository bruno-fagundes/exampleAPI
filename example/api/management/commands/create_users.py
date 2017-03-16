from django.core.management.base import BaseCommand

from example.api.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = ['Jose', 'Samuel', 'Andre', 'Regina']
        for user in users:
            username = user.lower()
            User.objects.create(username=username, email="{}@fagundes.com".format(username), first_name=user)
