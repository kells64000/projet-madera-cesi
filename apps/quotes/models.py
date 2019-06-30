# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from users.models import SalesPerson, Client
from components.models import House


class Quote(models.Model):

    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=255, null=True)
    reference = models.CharField(max_length=10, null=False, default='0000000000')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    state = models.TextField()
    attachment = models.FileField(_('attachment'), max_length=100, null=True, blank=True,
        default=None, upload_to='static/pdf/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # ForeignKeys
    client = models.ForeignKey(Client,
                               blank=False,
                               default=None,
                               null=True,
                               on_delete=models.DO_NOTHING,
                               related_name=_('client'))
    salesperson = models.ForeignKey(SalesPerson,
                                    blank=False,
                                    default=None,
                                    null=True,
                                    on_delete=models.DO_NOTHING,
                                    related_name=_('salesperson'))

    house = models.ForeignKey(House,
                              blank=False,
                              default=None,
                              null=True,
                              on_delete=models.DO_NOTHING,
                              related_name=_('house'))
