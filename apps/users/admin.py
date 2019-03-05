from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from .models import MaderaUser, Client, SalesPerson


class UserTypefilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('user type')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'type'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('client', _('client')),
            ('salesperson', _('vendeur')),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        if self.value() == 'client':
            return Client.objects.all()
        if self.value() == 'salesperson':
            return SalesPerson.objects.all()


@admin.register(MaderaUser)
class MaderaUserAdmin(UserAdmin):
    list_per_page = 20
    list_display = ('id_display', 'user_display', 'email_user_display', 'date_joined_display',
                    'address')
    fieldsets = (
        ('Personal info',
            {'fields':
                ('username', 'email', 'password', 'first_name', 'last_name', 'address')
             }
         ),
        ('Professionnel',
            {'fields': ()}
         ),
        ('Permissions',
            {'fields':
                ('is_active', 'is_staff', 'is_superuser', 'groups', )
             }
         ),
        ('Dates importantes',
            {'fields':
                ('date_joined',)
             }
         ),
    )

    raw_id_fields = ('address',)
    list_filter = ('is_active', 'is_staff', UserTypefilter)
    search_fields = ['^id', 'last_name', 'first_name', '^email']
    ordering = ('-id',)

    def id_display(self, obj):
        if obj.user.is_active:
            return format_html(
                u'<span style="color:#00FF00" class="glyphicon glyphicon-chevron-down"></span> {0}',  # NOQA
                obj.id
            )
        else:
            return format_html(
                u'<span style="color:#FF0000" class="glyphicon glyphicon-remove"></span> {0}',
                obj.id
            )
    id_display.short_description = "ID utilisateur"

    def user_display(self, obj):
        return format_html(
            u'<a href="../../users/maderauser/{0}" target="_blank">{1}  {2}</a>',
            obj.id,
            obj.first_name,
            obj.last_name)
    user_display.short_description = "Utilisateur"

    def email_user_display(self, obj):
        return format_html(
            u'<a href="../../users/maderauser/{0}" target="_blank">{1}</a>',
            obj.id,
            obj.email
        )
    email_user_display.short_description = "Email"

    def date_joined_display(self, obj):
        return format_html(
            u'{0}',
            obj.date_joined.strftime("%d/%m/%Y")
        )
    date_joined_display.short_description = "Date d'inscription"

    def last_con_display(self, obj):
        try:
            return format_html(
                u'{0}',
                obj.last_login.strftime("%d/%m/%Y")
            )
        except AttributeError:
            return ''
    last_con_display.short_description = "Derniere connexion"
