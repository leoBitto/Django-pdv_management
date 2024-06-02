from django import forms
from django.utils.translation import gettext_lazy as _
from .models import PDV, OpeningHours
import re

class PDVForm(forms.ModelForm):
    class Meta:
        model = PDV
        fields = ['name', 'address', 'phone']
        labels = {
            'name': _('Nome'),
            'address': _('Indirizzo'),
            'phone': _('Telefono'),
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Inserisci il nome')}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Inserisci l\'indirizzo')}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'type': 'tel', 'placeholder': _('Inserisci il numero di telefono')}),
        }


class OpeningHoursForm(forms.ModelForm):
    class Meta:
        model = OpeningHours
        fields = ['pdv', 'weekday', 'opening_time', 'closing_time', 'is_closed']
        labels = {
            'pdv': _('Negozio'),
            'weekday': _('Giorno della settimana'),
            'opening_time': _('Orario di apertura'),
            'closing_time': _('Orario di chiusura'),
            'is_closed': _('Giorno di chiusura'),
        }
        widgets = {
            'pdv': forms.Select(attrs={'class': 'form-control'}),
            'weekday': forms.Select(attrs={'class': 'form-control'}),
            'opening_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time', 'placeholder': _('Inserisci l\'orario di apertura')}),
            'closing_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time', 'placeholder': _('Inserisci l\'orario di chiusura')}),
            'is_closed': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

    def clean(self):
        cleaned_data = super().clean()
        opening_time = cleaned_data.get('opening_time')
        closing_time = cleaned_data.get('closing_time')
        is_closed = cleaned_data.get('is_closed')
        
        if is_closed:
            if opening_time or closing_time:
                raise forms.ValidationError(
                    _('Se il giorno è di chiusura, non devono essere forniti orari di apertura o chiusura.'),
                    code='invalid_times_when_closed'
                )
        else:
            if not opening_time or not closing_time:
                raise forms.ValidationError(
                    _('Se il giorno non è di chiusura, devono essere forniti sia l\'orario di apertura che l\'orario di chiusura.'),
                    code='missing_times'
                )
            if closing_time <= opening_time:
                raise forms.ValidationError(
                    _('L\'orario di chiusura deve essere successivo all\'orario di apertura.'),
                    code='invalid_closing_time'
                )
        
        return cleaned_data