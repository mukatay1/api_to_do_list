from django.apps import AppConfig


class SatusAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'satus_app'

    def ready(self):
        import satus_app.signals
