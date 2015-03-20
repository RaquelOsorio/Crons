__author__ = 'viviana'


from django import forms
from reglas.models import Crons
from reglas.models import MultiSelectFormField
from bootstrap3_datetime.widgets import DateTimePicker
from django.contrib.admin.widgets import AdminDateWidget, FilteredSelectMultiple


class CronsForm(forms.ModelForm):

    #reminder = forms.DateTimeField(label='hora',widget=DateTimePicker(options={"Default": 1,"format": "YYYY-MM-DD HH:mm", "pickTime": False}))
    class Meta:
        model= Crons
        exclude = ['nombre']
        #fields = ("accion","dispositivo","dia","hora")
        widgets = {
            'hora' : DateTimePicker(options={"icons":'glyphicon glyphicon-time',"format": "HH:mm","pickDate": False, "viewMode":'time', "showClose":'true'})
        }

class CronsFormulario(forms.ModelForm):

    #reminder = forms.DateTimeField(label='hora',widget=DateTimePicker(options={"Default": 1,"format": "YYYY-MM-DD HH:mm", "pickTime": False}))
    class Meta:
        model= Crons
        exclude = ['nombre']
        widgets = {
            'hora' : DateTimePicker(options={"icons":'glyphicon glyphicon-time',"format": "HH:mm","pickDate": False, "viewMode":'time', "showClose":'true'})
        }
        #widgets = {
        #    'hora' : forms.DateTimeField(required=False, widget=DateTimePicker(options={"format": "HH:mm","pickDate": False}))
        #}

        #fields = ("accion","dispositivo","dia","hora")

