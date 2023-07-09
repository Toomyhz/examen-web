from typing import Any
from django.forms import (
    Form,
    CharField,
    EmailField,
    TextInput,
    PasswordInput,
    EmailInput
)
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core import validators
from django.core.exceptions import ValidationError

class FormRegister(UserCreationForm):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget=PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Ingrese su contraseña'
            }
        )
        self.fields['password2'].widget=PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Ingrese su contraseña'
            }
        )

    first_name = CharField(label='Nombre', max_length=100, widget=TextInput(attrs={'class':'form-control'}))
    last_name = CharField(label='Apellido', max_length=100, widget=TextInput(attrs={'class':'form-control'}))

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name.isalpha():
            raise ValidationError("Ingrese solo caracteres alfabéticos en el nombre.")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not last_name.isalpha():
            raise ValidationError("Ingrese solo caracteres alfabéticos en el apellido.")
        return last_name
    
    class Meta:
        model=User
        fields=[
            'username',
            'first_name',
            'last_name',
            'email',
        ]
        widgets={
            'username':TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su nombre de usuario'
                }
            ),
            'email':EmailInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su correo electrónico'
                }
            )
        }

class FormLogin(Form):
    username=CharField(
        label="Nombre de usuario",
        max_length=50,
        required=True,
        widget=TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Ingrese su nombre de usuario'
            }
        )
    )
    password=CharField(
        label="Contraseña",
        max_length=50,
        required=True,
        widget=PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Ingrese su contraseña'
            }
        )
    )