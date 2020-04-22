from django.apps import AppConfig


class AuditAppConfig(AppConfig):
    name = 'audit_app'

    def ready(self):
        import audit_app.signals