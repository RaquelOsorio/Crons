__author__ = 'viviana'


from django import forms
from reglas.models import Crons
from reglas.models import MultiSelectFormField



class CronsForm(forms.ModelForm):
    class Meta:
        model= Crons
        fields = ("accion","dispositivo","dia","hora")
