# Generated by Django 2.2.24 on 2022-07-03 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_auto_20220701_0136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='new_building',
            field=models.BooleanField(db_index=True, null=True, verbose_name='Новостройка ли'),
        ),
    ]
