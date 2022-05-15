# Generated by Django 4.0 on 2022-05-10 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktable', '0010_delete_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=90)),
                ('email', models.CharField(default='', max_length=111)),
                ('date_book', models.DateField()),
                ('time', models.DateTimeField()),
                ('people', models.IntegerField(default=1)),
                ('message', models.CharField(default='', max_length=5000)),
            ],
        ),
    ]