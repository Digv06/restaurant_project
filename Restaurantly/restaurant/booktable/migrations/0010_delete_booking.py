# Generated by Django 4.0 on 2022-05-10 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktable', '0009_remove_booking_phone'),
    ]

    operations = [
        migrations.DeleteModel(
            name='booking',
        ),
    ]
