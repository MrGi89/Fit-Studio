# Generated by Django 2.0.2 on 2018-03-21 10:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('control_panel', '0007_auto_20180321_0845'),
    ]

    operations = [
        migrations.AddField(
            model_name='pass',
            name='start_date',
            field=models.DateField(default=datetime.date(2018, 3, 21), verbose_name='Data rozpoczęcia'),
        ),
        migrations.AlterField(
            model_name='pass',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='passes', to='control_panel.Member', verbose_name='Użytkownik'),
        ),
        migrations.AlterField(
            model_name='pass',
            name='product',
            field=models.ForeignKey(on_delete=None, to='control_panel.Product', verbose_name='Karnet'),
        ),
        migrations.AlterField(
            model_name='pass',
            name='status',
            field=models.SmallIntegerField(choices=[(1, 'paid'), (2, 'not paid')], default=2, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='product',
            name='validity',
            field=models.SmallIntegerField(default=30),
        ),
    ]
