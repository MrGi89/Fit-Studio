# Generated by Django 2.1.7 on 2019-03-19 21:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('control_panel', '0002_auto_20190319_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classtime',
            name='class_time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='member',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='mail',
            field=models.EmailField(blank=True, max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='hourly_rate',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='mail',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
    ]