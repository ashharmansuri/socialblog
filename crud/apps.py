from django.apps import AppConfig


class CrudConfig(AppConfig):
    name = 'crud'
    
    # for implementing signal
    def ready(self):
        import crud.signals
