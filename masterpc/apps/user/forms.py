from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import *

class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email']

        widgets = {
            'username': forms.TextInput(
                attrs = {
                    'class':'form-control bg-dark text-light my-2',
                    'placeholder':'Nombre de Usuario',
                    'id': 'username',
                    'autocapitalize':'none'
                }
            ),
            'email': forms.EmailInput(
                attrs = {
                    'class':'form-control bg-dark text-light my-2',
                    'placeholder':'Correo electronico',
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


class PcForm(forms.ModelForm):
    class Meta:
        model = Pc
        fields = ['name', 'budget']

        widgets = {
            'name': forms.TextInput(
                attrs = {
                    'class':'form-control mb-3',
                    'placeholder':'Nombre del PC',
                    # 'id': 'username',
                }
            ),
            'budget': forms.NumberInput(
                attrs = {
                    'class':'form-control mb-3',
                    'placeholder':'Presupuesto (Opcional)',
                    # 'id': 'username',
                }
            ),
        
        }
