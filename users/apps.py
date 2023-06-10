from django.apps import AppConfig
from django.db.models import BigAutoField


class UsersConfig(AppConfig):
    
    name = 'users'

    def ready(self):
        import users.signals