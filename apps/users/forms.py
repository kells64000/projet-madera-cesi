from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import MaderaUser, SalesPerson, Client


class UserForm(ModelForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class ProfileForm(ModelForm):

    class Meta:
        model = MaderaUser
        fields = ('location',)


class SalesPersonForm(ModelForm):

    class Meta:
        model = SalesPerson
        fields = ('workplace',)


class ClientForm(ModelForm):

    class Meta:
        model = Client
        fields = ('is_pro',)
