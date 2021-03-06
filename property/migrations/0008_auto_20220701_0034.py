# Generated by Django 2.2.24 on 2022-06-30 21:34

from django.db import migrations


def fill_owners_flats(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    flats = Flat.objects.all()
    for flat in flats.iterator():
        flat.owners.set(Owner.objects.filter(
            full_name=flat.owner,
            phonenumber=flat.owners_phonenumber
            )
        )


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_auto_20220630_2359'),
    ]

    operations = [
        migrations.RunPython(fill_owners_flats)
    ]
