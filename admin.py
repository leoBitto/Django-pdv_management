from django.contrib import admin
from .models import PDV, OpeningHours

@admin.register(PDV)
class PDVAdmin(admin.ModelAdmin):
    exclude=('code',)
    list_display = ('name', 'address', 'phone', 'code', 'id')
    search_fields = ('name', 'address', 'phone')

@admin.register(OpeningHours)
class OpeningHoursAdmin(admin.ModelAdmin):
    list_display = ('pdv', 'weekday', 'opening_time', 'closing_time')
    list_filter = ('pdv', 'weekday')
