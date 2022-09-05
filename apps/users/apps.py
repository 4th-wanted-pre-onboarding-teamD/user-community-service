from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.users'

    # admin 페이지 로그인 기록
    verbose_name = _('apps.users')
    def ready(self):
        import apps.users.signals