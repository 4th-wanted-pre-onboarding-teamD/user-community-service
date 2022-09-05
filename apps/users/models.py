from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models
from django.conf import settings
from model_utils.models import TimeStampedModel
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    GENDER_CHOICES = (('Male', '남성'), ('Female', '여성'))

    first_name = None
    last_name = None
    name = models.CharField(max_length=10)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=True, blank=True)
    age = models.IntegerField(validators=[MinValueValidator(1)], null=True, blank=True)
    phone = models.CharField(max_length=13, null=True, blank=True)

class UserLoginLog(TimeStampedModel):
    """ admin 페이지 로그인 기록 모델 - superuser 전용"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('User'),
        related_name='login_logs',
        blank=True,
        null=True,
        on_delete=models.DO_NOTHING,
    )
    ip_address = models.GenericIPAddressField(
        verbose_name=_('IP Address')
    )
    user_agent = models.CharField(
        verbose_name=_('HTTP User Agent'),
        max_length=300,
    )

    class Meta:
        verbose_name = _('user login log')
        verbose_name_plural = _('user login logs')
        ordering = ('-created',)

    def __str__(self):
        return '%s %s' % (self.user, self.ip_address)

class UserLog(models.Model):
    """유저 로그인 로그 기록 모델"""
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    login_date = models.DateTimeField("login_date", auto_now_add=True)