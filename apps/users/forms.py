import floppyforms.__future__ as forms

from django.forms import ModelForm

from .models import MaderaUser, SalesPerson, Client

USER_FORM_FIELDS = ['first_name', 'last_name', 'email', 'phone']


class UserForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True
        self.fields['phone'].required = True

    class Meta:
        model = MaderaUser
        fields = USER_FORM_FIELDS
        widgets = {
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput(),
            'email': forms.TextInput(),
            'phone': forms.TextInput()
        }

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        return cleaned_data


class SalesPersonForm(UserForm):

    class Meta:
        model = SalesPerson
        fields = ('workplace',)


class ClientForm(UserForm):

    class Meta:
        model = Client
        fields = ('is_pro',)
