from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email']

        widgets = {
            'username': forms.TextInput(
                attrs = {
                    'class':'form-control bg-dark text-light my-2',
                    # 'placeholder':'Nombre de Usuario',
                    'id': 'username',
                    'autocapitalize':'none'
                }
            ),
            'email': forms.EmailInput(
                attrs = {
                    'class':'form-control bg-dark text-light my-2',
                    # 'placeholder':'Correo electronico',
                    'id': 'email'
                }
            ),
        }

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Email already exists")
        return email
