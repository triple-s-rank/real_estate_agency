# Generated by Django 2.2.24 on 2022-06-30 22:32

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_auto_20220701_0034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='full_name',
            field=models.CharField(blank=True, db_index=True, max_length=150, verbose_name='ФИО владельца'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='phonenumber',
            field=models.CharField(db_index=True, max_length=20, verbose_name='Номер владельца'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='pure_phonenumber',
            field=phonenumber_field.modelfields.PhoneNumberField(db_index=True, max_length=128, region=None, verbose_name='Нормлизованный номер владельца'),
        ),
    ]
