# Generated by Django 2.0.2 on 2018-03-21 11:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control_panel', '0008_auto_20180321_1048'),
    ]

    operations = [
        migrations.AddField(
            model_name='pass',
            name='end_date',
            field=models.DateField(default=datetime.date(2018, 3, 21)),
        ),
    ]
