# Generated by Django 5.0 on 2024-05-23 12:57

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PDV',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('code', models.CharField(blank=True, default='', max_length=20, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Punti Vendita',
            },
        ),
        migrations.CreateModel(
            name='OpeningHours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekday', models.CharField(choices=[('monday', 'Lunedì'), ('tuesday', 'Martedì'), ('wednesday', 'Mercoledì'), ('thursday', 'Giovedì'), ('friday', 'Venerdì'), ('saturday', 'Sabato'), ('sunday', 'Domenica')], max_length=10, verbose_name='Giorno della settimana')),
                ('opening_time', models.TimeField(verbose_name='Orario di apertura')),
                ('closing_time', models.TimeField(verbose_name='Orario di chiusura')),
                ('pdv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opening_hours', to='pdv_management.pdv', verbose_name='PDV')),
            ],
            options={
                'verbose_name': 'Orario di apertura',
                'verbose_name_plural': 'Orari di apertura',
            },
        ),
    ]
