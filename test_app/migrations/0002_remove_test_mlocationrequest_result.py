# Generated by Django 4.0.4 on 2022-06-07 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='mLocationRequest_result',
        ),
    ]
