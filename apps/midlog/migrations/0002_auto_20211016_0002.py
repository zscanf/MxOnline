# Generated by Django 2.0.2 on 2021-10-16 00:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('midlog', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AccessTimeOutLogs',
        ),
        migrations.DeleteModel(
            name='OpLogs',
        ),
    ]
