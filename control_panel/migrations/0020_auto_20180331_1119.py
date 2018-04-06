# Generated by Django 2.0.2 on 2018-03-31 11:19

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('control_panel', '0019_auto_20180328_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='current_pass',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='control_panel.Pass'),
        ),
        migrations.AlterField(
            model_name='pass',
            name='start_date',
            field=models.DateField(default=datetime.date(2018, 3, 31), verbose_name='Data rozpoczęcia'),
        ),
    ]