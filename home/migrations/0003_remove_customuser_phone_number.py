# Generated by Django 5.1.4 on 2024-12-27 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_customuser_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='phone_number',
        ),
    ]
