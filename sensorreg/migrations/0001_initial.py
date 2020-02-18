# Generated by Django 3.0.3 on 2020-02-18 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID', models.IntegerField()),
                ('IP', models.GenericIPAddressField(protocol='IPv4')),
                ('Port', models.IntegerField()),
                ('MacAddress', models.CharField(max_length=100)),
                ('AdministrativeRegion', models.CharField(choices=[('gangwon-do', 'Gangwon-do'), ('gyeonggi-do', 'Gyeongii-do')], max_length=100)),
                ('InstallationRoute', models.CharField(choices=[('a', 'A'), ('b', 'B')], max_length=100)),
                ('InstallationLocation', models.CharField(max_length=100)),
                ('GPSCoordinates', models.FloatField()),
                ('InterlockDeviceInformation', models.CharField(max_length=100)),
            ],
        ),
    ]
