from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class HoodConfig(AppConfig):
    name = 'hood'
    verbose_name = ('hood')

    def ready(self):
        import hood.signals
