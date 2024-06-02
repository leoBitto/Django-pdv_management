from django.core.exceptions import ValidationError
import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
class PDV(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(
        max_length=20,
        blank=True,
        validators=[RegexValidator(
            regex=r'^\d{10}$',
            message=_("Il numero di telefono deve contenere 10 cifre.")
        )])
    code = models.CharField(max_length=20, unique=True, blank=True, default="")

    def generate_code(self):
        if not self.code:
            self.code = f"PDV-{self.id.hex[:8].upper()}"  # Usa i primi 8 caratteri dell'UUID come codice

    def save(self, *args, **kwargs):
        if not self.code:
            self.generate_code()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Punti Vendita"

    def __str__(self):
        return self.name


class OpeningHours(models.Model):
    WEEKDAY_CHOICES = [
        ('monday', 'Lunedì'),
        ('tuesday', 'Martedì'),
        ('wednesday', 'Mercoledì'),
        ('thursday', 'Giovedì'),
        ('friday', 'Venerdì'),
        ('saturday', 'Sabato'),
        ('sunday', 'Domenica'),
    ]

    pdv = models.ForeignKey(PDV, related_name='opening_hours', on_delete=models.CASCADE, verbose_name=_("PDV"))
    weekday = models.CharField(max_length=10, choices=WEEKDAY_CHOICES, verbose_name=_("Giorno della settimana"))
    opening_time = models.TimeField(verbose_name=_("Orario di apertura"))
    closing_time = models.TimeField(verbose_name=_("Orario di chiusura"))
    is_closed = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Orario di apertura")
        verbose_name_plural = _("Orari di apertura")

    def __str__(self):
        return f"{self.get_weekday_display()}: {self.opening_time} - {self.closing_time}"
    
    def clean(self):
        if self.opening_time >= self.closing_time:
            raise ValidationError(_("L'orario di apertura deve essere prima dell'orario di chiusura."))



