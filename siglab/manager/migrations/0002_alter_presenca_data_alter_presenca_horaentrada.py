# Generated by Django 5.1.1 on 2025-01-27 19:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presenca',
            name='data',
            field=models.DateField(default=datetime.datetime(2025, 1, 27, 19, 16, 0, 889121, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='presenca',
            name='horaEntrada',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 27, 19, 16, 0, 951603, tzinfo=datetime.timezone.utc)),
        ),
    ]
