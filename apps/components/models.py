from decimal import Decimal
from django.db import models
from django.utils.translation import ugettext_lazy as _

from users.models import MaderaUser


class Component(models.Model):

    name = models.CharField(_('name'), max_length=30, blank=False, null=False)
    nature = models.CharField(_('nature'), max_length=20)
    length = models.DecimalField(_('length'), max_digits=8,
                                 decimal_places=2, blank=False, null=False)
    width = models.DecimalField(_('width'), max_digits=8,
                                decimal_places=2, blank=False, null=False)
    depth = models.DecimalField(_('depth'), max_digits=8, decimal_places=2, null=True)
    unit = models.CharField(_('unit'), max_length=10, blank=False, null=False)
    price = models.DecimalField(_('price'), max_digits=10, decimal_places=2, null=True)

    # ForeignKeys
    designer = models.ForeignKey(MaderaUser,
                                 blank=True,
                                 default=None,
                                 null=True,
                                 on_delete=models.DO_NOTHING,
                                 related_name=_('designer'))

    @property
    def surface(self):
        return (self.length * self.width * (self.depth if self.depth else 1)
                ).quantize(Decimal(10) ** -2)

    def dimensions_verbose(self):
        return 'Dimensions for {n}: length {l} x width {w}'.format(n=self.name,
                                                                   l=self.length,
                                                                   w=self.width)

    @property
    def designed_by(self):
        if self.designer:
            return self.designer.get_full_name
        return None
