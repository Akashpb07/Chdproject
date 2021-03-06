# Generated by Django 3.0.4 on 2020-05-04 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webapp', '0010_eye'),
    ]

    operations = [
        migrations.CreateModel(
            name='blooddonor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=20)),
                ('blood_group', models.CharField(max_length=20)),
                ('mobile_no', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
            ],
        ),
    ]
