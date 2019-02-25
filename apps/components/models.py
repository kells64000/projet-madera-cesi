from django.db import models
from django.utils.translation import ugettext_lazy as _

from users.models import MaderaUser


class Component(models.Model):

    name = models.CharField(_('name'), max_length=30, blank=False, null=False)
    nature = models.CharField(_('nature'), max_length=10)
    length = models.DecimalField(_('length'), max_digits=3,
                                 decimal_places=2, blank=False, null=False)
    width = models.DecimalField(_('width'), max_digits=3,
                                decimal_places=2, blank=False, null=False)
    depth = models.DecimalField(_('depth'), max_digits=3, decimal_places=2,)
    unit = models.CharField(_('unit'), max_length=10)

    # ForeignKeys
    designer = models.ForeignKey(MaderaUser,
                                 blank=True,
                                 default=None,
                                 null=True,
                                 on_delete=models.CASCADE,
                                 related_name=_('designer'))

    def surface(self):
        return self.legnth * self.width * (self.depth if self.depth else 1)

    def dimensions_verbose(self):
        return 'Dimensions for {n}: length {l} x width {w}'.format(n=self.name,
                                                                   l=self.length,
                                                                   w=self.width)

    def designed_by(self):
        return self.designer.get_full_name()
