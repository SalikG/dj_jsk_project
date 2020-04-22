from django.apps import AppConfig


class LoginAppConfig(AppConfig):
    name = 'login_app'

    def ready(self):
        from .signals import create_user_profile