# Generated by Django 3.0.4 on 2020-05-04 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webapp', '0012_auto_20200504_1657'),
    ]

    operations = [
        migrations.CreateModel(
            name='bone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drimg', models.ImageField(upload_to='drpics')),
                ('name', models.CharField(max_length=100)),
                ('speciality', models.CharField(max_length=100)),
                ('deprtimg', models.ImageField(upload_to='drpics')),
                ('department', models.CharField(max_length=100)),
                ('location', models.TextField(max_length=100)),
                ('mobNo', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='dermatology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drimg', models.ImageField(upload_to='drpics')),
                ('name', models.CharField(max_length=100)),
                ('speciality', models.CharField(max_length=100)),
                ('deprtimg', models.ImageField(upload_to='drpics')),
                ('department', models.CharField(max_length=100)),
                ('location', models.TextField(max_length=100)),
                ('mobNo', models.CharField(max_length=15)),
            ],
        ),
        migrations.AlterField(
            model_name='eye',
            name='deprtimg',
            field=models.ImageField(upload_to='drpics'),
        ),
        migrations.AlterField(
            model_name='eye',
            name='drimg',
            field=models.ImageField(upload_to='drpics'),
        ),
    ]
