# Generated by Django 4.0 on 2022-05-10 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktable', '0003_alter_booking_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='email',
            field=models.CharField(default='', max_length=111),
        ),
        migrations.AlterField(
            model_name='booking',
            name='message',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AlterField(
            model_name='booking',
            name='name',
            field=models.CharField(default='', max_length=90),
        ),
        migrations.AlterField(
            model_name='booking',
            name='phone',
            field=models.CharField(default='', max_length=10),
        ),
    ]
