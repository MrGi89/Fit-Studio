# Generated by Django 2.1.7 on 2019-03-24 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control_panel', '0006_auto_20190319_2239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='products',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='trainers',
        ),
    ]
