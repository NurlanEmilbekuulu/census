# Generated by Django 3.1.1 on 2020-10-27 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('census', '0009_auto_20201027_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='photo',
            field=models.ImageField(upload_to='employee/photos', verbose_name='сүрөт'),
        ),
    ]
