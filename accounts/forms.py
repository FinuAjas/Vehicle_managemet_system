from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm
from . models import Account


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update(
                {'class': 'form-control form-control-lg'})


