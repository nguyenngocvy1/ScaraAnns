from django.apps import AppConfig


class MyModel1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'my_model1'
