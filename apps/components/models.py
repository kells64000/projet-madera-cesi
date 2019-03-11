from decimal import Decimal
from django.db import models
from django.utils.translation import ugettext_lazy as _

from users.models import MaderaUser
from .constants import FAMILY_CHOICES, NATURE_CHOICES, GAMME_CHOICES, SHAPE_CHOICES


class Gamme(models.Model):

    name = models.CharField(_('name'), max_length=30, blank=False, null=False,
        choices=GAMME_CHOICES)
    ratio = models.DecimalField(_('length'), max_digits=4,
                                decimal_places=2, blank=False, null=True)


class Component(models.Model):

    name = models.CharField(_('name'), max_length=30, blank=False, null=False)
    component_type = models.CharField(_('type'), max_length=30, blank=False, null=True)
    nature = models.CharField(_('nature'), max_length=3, choices=NATURE_CHOICES)
    length = models.DecimalField(_('length'), max_digits=8,
                                 decimal_places=2, blank=False, null=True)
    width = models.DecimalField(_('width'), max_digits=8,
                                decimal_places=2, blank=False, null=True)
    depth = models.DecimalField(_('depth'), max_digits=8, decimal_places=2, null=True)
    unit = models.CharField(_('unit'), max_length=10, blank=False, null=True)
    price = models.DecimalField(_('price'), max_digits=10, decimal_places=2, null=True)
    total_price = models.DecimalField(_('total_price'), max_digits=10, decimal_places=2, null=True)
    quantity = models.IntegerField(_('quantity'), blank=False, null=True)

    gammes = models.ManyToManyField(Gamme)

    @property
    def surface(self):
        return (self.length * self.width).quantize(Decimal(10) ** -2)

    @property
    def total_price(self):
        return self.price * self.quantity if self.quantity and self.price else None

    def dimensions_verbose(self):
        return 'Dimensions for {n}: length {l} x width {w}'.format(n=self.name, l=self.length)

    def get_gammes(self):
        if hasattr(self, "gammes"):
            gammes = self.gammes
        else:
            gammes = self.gammes.all()
            setattr(self, "gammes", gammes)
        return gammes


class Module(models.Model):

    name = models.CharField(_('name'), max_length=30, blank=False, null=False)
    nature = models.CharField(_('nature'), max_length=20)
    length = models.DecimalField(_('length'), max_digits=8,
                                 decimal_places=2, blank=False, null=True)
    length2 = models.DecimalField(_('length'), max_digits=8,
                                  decimal_places=2, blank=False, null=True)
    height = models.DecimalField(_('width'), max_digits=8,
                                decimal_places=2, blank=False, null=True)
    angle = models.IntegerField(_('angle'), blank=False, null=True)
    angle_type = models.CharField(_('angle_type'), max_length=20, null=True)
    unit = models.CharField(_('unit'), max_length=10, blank=False, null=True)
    price = models.DecimalField(_('price'), max_digits=10, decimal_places=2, null=True)
    family = models.CharField(_('family'), max_length=3, choices=FAMILY_CHOICES, null=True)
    quantity = models.IntegerField(_('quantity'), blank=False, null=True)

    # ForeignKeys
    designer = models.ForeignKey(MaderaUser,
                                 blank=True,
                                 default=None,
                                 null=True,
                                 on_delete=models.DO_NOTHING,
                                 related_name=_('designer'))

    gammes = models.ManyToManyField(Gamme)
    components = models.ManyToManyField(Component)

    @property
    def designed_by(self):
        if self.designer:
            return self.designer.get_full_name
        return None

    @property
    def surface(self):
        if self.length and self.height:
            return (self.length * self.height).quantize(Decimal(10) ** -2)

    def dimensions_verbose(self):
        return 'Dimensions for {n}: length {l} x height {h}'.format(n=self.name,
            l=self.length, h=self.height)

    def get_components(self):
        if hasattr(self, "components"):
            components = self.components
        else:
            components = self.components.all()
            setattr(self, "components", components)
        return components

    def get_gammes(self):
        if hasattr(self, "gammes"):
            gammes = self.gammes
        else:
            gammes = self.gammes.all()
            setattr(self, "gammes", gammes)
        return gammes

    @property
    def calculated_price(self):
        price = 0
        for comp in self.components.all():
            if comp.total_price:
                price += comp.total_price
        return price

    @property
    def total_price(self):
        return (self.calculated_price * self.quantity if self.quantity and
            self.calculated_priceprice else None)


class House(models.Model):

    shape = models.CharField(_('shape'), max_length=3, choices=SHAPE_CHOICES)
    shape_img = models.FileField(_('shape_img'), max_length=100, null=True)
    gamme = models.ManyToManyField(Gamme)
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

    @property
    def total_price(self):
        price = 0
        for module in self.modules.all():
            if module.total_price:
                price += module.total_price
        return price
