# Generated by Django 4.0 on 2022-05-10 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktable', '0005_remove_booking_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='phone',
            field=models.CharField(default='', max_length=10),
        ),
    ]
