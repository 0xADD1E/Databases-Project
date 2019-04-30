from django.apps import AppConfig
from django.contrib import admin


class FrontendConfig(AppConfig):
    name = 'frontend'

    def ready(self):
        models = self.get_models()
        for model in models:
            try:
                admin.site.register(model)
            except admin.sites.AlreadyRegistered:
                pass
