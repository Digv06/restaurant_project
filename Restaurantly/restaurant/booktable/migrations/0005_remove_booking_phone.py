# Generated by Django 4.0 on 2022-05-10 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktable', '0004_alter_booking_email_alter_booking_message_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='phone',
        ),
    ]
