from __future__ import unicode_literals

from django.db import models
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin)
from django.utils import timezone
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _

from addresses.models import Address
from .managers import UserManager


class MaderaUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('email address'), unique=True, null=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    phone = models.CharField(_('phone'), max_length=12, null=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('is_staff'), default=False)
    avatar = models.ImageField(upload_to=settings.AVATAR_URL, null=True, blank=True)

    # ForeignKeys
    address = models.ForeignKey(Address,
                                blank=True,
                                default=None,
                                null=True,
                                on_delete=models.CASCADE)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    @property
    def username(self):
        return getattr(self, self.USERNAME_FIELD)

    @cached_property
    def user(self):
        # Support for self as profile. Use of this is deprecated
        return self

    @property
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
    company = models.CharField(_('company'), max_length=50, blank=True)

    def _is_pro(self):
        '''
        Returns bool about whether the client is pro or not
        '''
        return self.is_pro

    def get_company(self):
        '''
        Returns client's company if any
        '''
        return self.company


class Provider(models.Model):

    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    phone = models.CharField(_('phone'), max_length=12, blank=True, unique=True)

    # ForeignKeys
    address = models.ForeignKey(Address,
                                blank=True,
                                default=None,
                                null=True,
                                on_delete=models.CASCADE)

    @property
    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name
