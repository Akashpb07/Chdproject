# Generated by Django 3.0.4 on 2020-05-04 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webapp', '0011_blooddonor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blooddonor',
            name='mobile_no',
            field=models.CharField(max_length=15),
        ),
    ]