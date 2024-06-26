# Generated by Django 5.0.4 on 2024-05-01 21:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_id', models.CharField(max_length=100)),
                ('device_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.device')),
            ],
        ),
        migrations.CreateModel(
            name='SensorDataFloat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('time', models.DateField()),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.sensor')),
            ],
        ),
        migrations.CreateModel(
            name='SensorDataText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=100)),
                ('time', models.DateField()),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.sensor')),
            ],
        ),
    ]
