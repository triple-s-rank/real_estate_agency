# Generated by Django 2.2.24 on 2022-06-30 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_auto_20220630_1727'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='new_building',
        ),
    ]
