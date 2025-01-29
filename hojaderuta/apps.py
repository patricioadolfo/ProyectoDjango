from django.apps import AppConfig


class HojaderutaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hojaderuta'

    def ready(self,):

        import hojaderuta.signals