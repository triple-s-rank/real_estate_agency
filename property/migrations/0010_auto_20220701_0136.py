# Generated by Django 2.2.24 on 2022-06-30 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_auto_20220701_0132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owner_pure_phone',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owners_phonenumber',
        ),
    ]
