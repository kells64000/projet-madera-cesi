from decimal import Decimal
from django.db import models
from django.utils.translation import ugettext_lazy as _

from users.models import MaderaUser
from .constants import FAMILY_CHOICES, NATURE_CHOICES, SHAPE_CHOICES


class Component(models.Model):

    name = models.CharField(_('name'), max_length=30, blank=False, null=False)
    nature = models.CharField(_('nature'), max_length=3, choices=NATURE_CHOICES)
    length = models.DecimalField(_('length'), max_digits=8,
                                 decimal_places=2, blank=False, null=True)
    width = models.DecimalField(_('width'), max_digits=8,
                                decimal_places=2, blank=False, null=True)
    depth = models.DecimalField(_('depth'), max_digits=8, decimal_places=2, null=True)
    unit = models.CharField(_('unit'), max_length=10, blank=False, null=True)
    price = models.DecimalField(_('price'), max_digits=10, decimal_places=2, null=True)

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
                                 decimal_places=2, blank=False, null=True)
    width = models.DecimalField(_('width'), max_digits=8,
                                decimal_places=2, blank=False, null=True)
    depth = models.DecimalField(_('depth'), max_digits=8, decimal_places=2, null=True)
    unit = models.CharField(_('unit'), max_length=10, blank=False, null=True)
    price = models.DecimalField(_('price'), max_digits=10, decimal_places=2, null=True)
    family = models.CharField(_('family'), max_length=3, choices=FAMILY_CHOICES, null=True)

    # ForeignKeys
    designer = models.ForeignKey(MaderaUser,
                                 blank=True,
                                 default=None,
                                 null=True,
                                 on_delete=models.DO_NOTHING,
                                 related_name=_('designer'))

    components = models.ManyToManyField(Component)

    @property
    def designed_by(self):
        if self.designer:
            return self.designer.get_full_name
        return None

    @property
    def surface(self):
        if self.length and self.width:
            return (self.length * self.width * (self.depth if self.depth else 1)
                    ).quantize(Decimal(10) ** -2)

    def dimensions_verbose(self):
        return 'Dimensions for {n}: length {l} x width {w}'.format(n=self.name,
                                                                   l=self.length,
                                                                   w=self.width)

    def get_components(self):
        if hasattr(self, "components"):
            components = self.components
        else:
            components = self.components.all()
            setattr(self, "components", components)
        return components


class Gamme(models.Model):

    name = models.CharField(_('name'), max_length=30, blank=False, null=False)
    nature = models.CharField(_('nature'), max_length=20, null=True)
    ratio = models.DecimalField(_('length'), max_digits=4,
                                decimal_places=2, blank=False, null=True)

    # ForeignKeys
    modules = models.ManyToManyField(Module)

    def get_modules(self):
        if hasattr(self, "modules"):
            modules = self.modules
        else:
            modules = self.modules.all().exclude(components="")
            setattr(self, "modules", modules)
        return modules

    def get_modules_by_nature(self):
        modules = Module.objects.filter(nature=self.nature)
        return modules


class House(models.Model):

    shape = models.CharField(_('shape'), max_length=3, choices=SHAPE_CHOICES)
    shape_img = models.FileField(_('shape_img'), max_length=100, null=True)

    # ForeignKeys
    modules = models.ManyToManyField(Module)

    def get_modules(self):
        if hasattr(self, "modules"):
            modules = self.modules
        else:
            modules = self.modules.all().exclude(components="")
            setattr(self, "modules", modules)
        return modules
