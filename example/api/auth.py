from .models import User


class AlwaysRootBackend(object):
    def authenticate(self, *args, **kwargs):
        return User.objects.get(username='bruno')

    def get_user(self, user_id):
        return User.objects.get(username='bruno')
