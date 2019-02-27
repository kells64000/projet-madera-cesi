from django.db import models
from django.utils.translation import ugettext_lazy as _
from users.models import MaderaUser




class Quote(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    state = models.TextField()
    attachment = models.TextField(null=True, blank=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # ForeignKeys
    customer = models.ForeignKey(MaderaUser,
                                 blank=False,
                                 default=None,
                                 null=False,
                                 on_delete=models.DO_NOTHING,
                                 related_name=_('customer'))
    salesman = models.ForeignKey(MaderaUser,
                                 blank=False,
                                 default=None,
                                 null=False,
                                 on_delete=models.DO_NOTHING,
                                 related_name=_('salesman'))
