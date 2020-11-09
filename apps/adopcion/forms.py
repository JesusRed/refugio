# -*- encoding:utf-8 -*-
from django import forms

from apps.adopcion.models import Persona, Solicitud


class PersonaForm(forms.ModelForm):

    class Meta:
        model = Persona
        fields = [
            'nombre',
            'apellidos',
            'edad',
            'telefono',
            'email',
            'domicilio',
        ]
        labels = {
            'nombre': 'Nombre',
            'apellidos': 'Apellidos',
            'edad': 'Edad',
            'telefono': 'Teléfono',
            'email': 'Correo electrónico',
            'domicilio': 'Domicilio',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'input-group-field'}),
            'apellidos': forms.TextInput(attrs={'class': 'input-group-field'}),
            'edad': forms.TextInput(attrs={'class': 'input-group-field'}),
            'telefono': forms.TextInput(attrs={'class': 'input-group-field'}),
            'email': forms.TextInput(attrs={'class': 'input-group-field'}),
            'domicilio': forms.Textarea(),
        }


class SolicitudForm(forms.ModelForm):

    class Meta:
        model = Solicitud
        fields = [
            'numero_mascotas',
            'razones',
        ]
        labels = {
            'numero_mascotas': 'Numero de mascotas',
            'razones': 'Razones para adoptar',

        }
        widgets = {
            'numero_mascotas': forms.TextInput(attrs={'class': 'input-group-field'}),
            'razones': forms.Textarea(attrs={'class': 'input-group-field'}),
        }
