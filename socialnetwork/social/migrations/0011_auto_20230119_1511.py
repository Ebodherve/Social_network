# Generated by Django 2.2.14 on 2023-01-19 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0010_auto_20230119_1436'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='notfication_type',
            new_name='notification_type',
        ),
    ]
