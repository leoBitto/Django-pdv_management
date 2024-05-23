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
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': _('Inserisci l\'indirizzo')}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'type': 'tel', 'placeholder': _('Inserisci il numero di telefono')}),
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        # Regex per validare il numero di telefono italiano (formato per Prato)
        phone_regex = r'^\+?39?(0|3)?[ .]?(57|59|55|571|571|573|574|575|577|578|79|77|78|80|81|82|572|570|586|579|580|581|582|583|584|585|588|585|587|586|589|572|570|573|574|577|571|578|575|578|79|77|78|80|81|82|85|88|89|00|01|02|03|04|05|06|07|08|09|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25|26|27|28|29|30|31|32|33|34|35|36|37|38|39|40|41|42|43|44|45|46|47|48|49|50|51|52|53|54|55|56|57|58|59|60|61|62|63|64|65|66|67|68|69|70|71|72|73|74|75|76|77|78|79|80|81|82|83|84|85|86|87|88|89|90|91|92|93|94|95|96|97|98|99)[ .]?[0-9]{6,8}$'
        if not re.match(phone_regex, phone):
            raise forms.ValidationError(_('Il numero di telefono non è valido. Assicurati di inserire un numero italiano valido.'))
        return phone

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
            'opening_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time', 'placeholder': _('Inserisci l\'orario di apertura')}),
            'closing_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time', 'placeholder': _('Inserisci l\'orario di chiusura')}),
        }

    def clean(self):
        cleaned_data = super().clean()
        opening_time = cleaned_data.get('opening_time')
        closing_time = cleaned_data.get('closing_time')
        if opening_time and closing_time:
            if closing_time <= opening_time:
                raise forms.ValidationError(_('L\'orario di chiusura deve essere successivo all\'orario di apertura.'), code='invalid_closing_time')
        return cleaned_data