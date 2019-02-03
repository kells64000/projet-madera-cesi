from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager


class MaderaUser(AbstractBaseUser, PermissionsMixin):
    # user = models.OneToOneField(User, related_name="madera_user", primary_key=True,
    #                             on_delete="cascade")
    username = models.CharField(_('username'), max_length=50, blank=False, default='unknown')
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    location = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('is_staff'), default=False)
    # avatar = models.ImageField(upload_to=settings.AVATAR_URL, null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)


class SalesPerson(MaderaUser):
    workplace = models.CharField(_('workplace'), max_length=20, blank=True)

    def get_worplace(self):
        '''
        Returns city in which salesperson works
        '''
        return self.workplace


class Client(MaderaUser):
    is_pro = models.BooleanField(_('is pro'), default=False)

    def _is_pro(self):
        '''
        Returns bool about whether the client is pro or not
        '''
        return self.is_pro
