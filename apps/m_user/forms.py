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
            'first_name':TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su nombre'
                }
            ),
            'last_name':TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su apellido'
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