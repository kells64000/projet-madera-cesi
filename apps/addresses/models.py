from django_countries import fields
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Address(models.Model):

    street = models.TextField(_(u'Adresse'))
    zipcode = models.CharField(_(u'Code postal'), max_length=10)
    city = models.CharField(_(u'Ville'), max_length=50)
    country = fields.CountryField(_(u'Pays'), max_length=2, default='FR')

    def verbose(self):
        return '%s (%s)' % (self.city.title(), self.zipcode[:2])

    def full_address(self):
        return u"{}, {} {}, {}".format(
            self.street.replace("\n", "").replace("\r", ""),
            self.city,
            self.zipcode,
            self.country.name).strip()

    def _get_department(self):
        return self.zipcode[0:2]
    department = property(_get_department)

    def should_display_department(self):
        return False
        # the following code should work but all the address have country as
        # FR so it failed, fix the google post form first and correct the
        # address of every vehicules
        if self.country.code.upper() in ('FR', ):
            return True
        return False

    def __unicode__(self):
        return '%s\n%s %s\n%s' % (
            self.street, self.zipcode, self.city, self.country)

    class Meta:
        verbose_name = _(u'Adresse')
        verbose_name_plural = _(u'Adresses')
