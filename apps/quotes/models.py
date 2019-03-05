# -*- coding: utf-8 -*-
import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _
from users.models import SalesPerson, Client


class Quote(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    state = models.TextField()
    attachment = models.TextField(null=True, blank=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # ForeignKeys
    client = models.ForeignKey(Client,
                               blank=False,
                               default=None,
                               null=False,
                               on_delete=models.DO_NOTHING,
                               related_name=_('client'))
    salesperson = models.ForeignKey(SalesPerson,
                                    blank=False,
                                    default=None,
                                    null=False,
                                    on_delete=models.DO_NOTHING,
                                    related_name=_('salesperson'))
