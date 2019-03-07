from decimal import Decimal
from django.db import models
from django.utils.translation import ugettext_lazy as _

from users.models import MaderaUser
from .constants import FAMILY_CHOICES, NATURE_CHOICES


class Component(models.Model):

    name = models.CharField(_('name'), max_length=30, blank=False, null=False)
    nature = models.CharField(_('nature'), max_length=3, choices=NATURE_CHOICES)
    length = models.DecimalField(_('length'), max_digits=8,
                                 decimal_places=2, blank=False, null=False)
    width = models.DecimalField(_('width'), max_digits=8,
                                decimal_places=2, blank=False, null=False)
    depth = models.DecimalField(_('depth'), max_digits=8, decimal_places=2, null=True)
    unit = models.CharField(_('unit'), max_length=10, blank=False, null=False)
    price = models.DecimalField(_('price'), max_digits=10, decimal_places=2, null=True)
    family = models.CharField(_('family'), max_length=3, choices=FAMILY_CHOICES, null=True)

    @property
    def surface(self):
        return (self.length * self.width * (self.depth if self.depth else 1)
                ).quantize(Decimal(10) ** -2)

    def dimensions_verbose(self):
        return 'Dimensions for {n}: length {l} x width {w}'.format(n=self.name,
                                                                   l=self.length,
                                                                   w=self.width)


class Module(models.Model):

    name = models.CharField(_('name'), max_length=30, blank=False, null=False)
    nature = models.CharField(_('nature'), max_length=20)
    length = models.DecimalField(_('length'), max_digits=8,
                                 decimal_places=2, blank=False, null=False)
    width = models.DecimalField(_('width'), max_digits=8,
                                decimal_places=2, blank=False, null=False)
    depth = models.DecimalField(_('depth'), max_digits=8, decimal_places=2, null=True)
    unit = models.CharField(_('unit'), max_length=10, blank=False, null=False)
    price = models.DecimalField(_('price'), max_digits=10, decimal_places=2, null=True)
    designer = models.ForeignKey(MaderaUser,
                                 blank=True,
                                 default=None,
                                 null=True,
                                 on_delete=models.DO_NOTHING,
                                 related_name=_('designer'))

    # ForeignKeys
    component = models.ForeignKey(Component,
                                blank=True,
                                default=None,
                                null=True,
                                on_delete=models.CASCADE,
                                related_name=_('mod_component'))

    @property
    def designed_by(self):
        if self.designer:
            return self.designer.get_full_name
        return None

    @property
    def surface(self):
        return (self.length * self.width * (self.depth if self.depth else 1)
                ).quantize(Decimal(10) ** -2)

    def dimensions_verbose(self):
        return 'Dimensions for {n}: length {l} x width {w}'.format(n=self.name,
                                                                   l=self.length,
                                                                   w=self.width)


class Gamme(models.Model):

    name = models.CharField(_('name'), max_length=30, blank=False, null=False)
    nature = models.CharField(_('nature'), max_length=20, null=True)

    # ForeignKeys
    module = models.ForeignKey(Module,
                               blank=True,
                               default=None,
                               null=True,
                               on_delete=models.CASCADE,
                               related_name=_('module'))
