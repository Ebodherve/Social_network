# Generated by Django 2.2.14 on 2023-01-18 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, default='/uploads/profile_pictures/default.png', upload_to='uploads/profile_pictures'),
        ),
    ]
