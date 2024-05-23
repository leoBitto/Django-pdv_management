from django import forms
from django.utils.translation import gettext_lazy as _
from .models import PDV, OpeningHours

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
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'type': 'tel'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder': _('Inserisci il nome')})
        self.fields['address'].widget.attrs.update({'placeholder': _('Inserisci l\'indirizzo')})
        self.fields['phone'].widget.attrs.update({'placeholder': _('Inserisci il numero di telefono')})

class OpeningHoursForm(forms.ModelForm):
    class Meta:
        model = OpeningHours
        fields = ['weekday', 'opening_time', 'closing_time']
        labels = {
            'weekday': _('Giorno della settimana'),
            'opening_time': _('Orario di apertura'),
            'closing_time': _('Orario di chiusura'),
        }
        widgets = {
            'weekday': forms.Select(attrs={'class': 'form-control'}),
            'opening_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'closing_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['opening_time'].widget.attrs.update({'placeholder': _('Inserisci l\'orario di apertura')})
        self.fields['closing_time'].widget.attrs.update({'placeholder': _('Inserisci l\'orario di chiusura')})
