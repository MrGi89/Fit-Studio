# Generated by Django 2.2.2 on 2019-06-27 08:27

import control_panel.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control_panel', '0004_auto_20190624_0823'),
    ]

    operations = [
        migrations.CreateModel(
            name='Studio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=200)),
                ('street', models.CharField(max_length=50)),
                ('postal_code', models.CharField(max_length=5)),
                ('city', models.CharField(max_length=50)),
                ('nip', models.PositiveIntegerField()),
                ('regon', models.PositiveIntegerField(blank=True, null=True)),
                ('mail', models.EmailField(max_length=254)),
                ('phone', models.PositiveIntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='group',
            name='color',
            field=control_panel.models.ColorField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='mail',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
    ]
