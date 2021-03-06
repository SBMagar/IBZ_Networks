# Generated by Django 3.0.4 on 2020-03-20 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='in_out_Window',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Black_Ice_Appearance', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('Black_Ice_Appearance_Operator', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('Action_Status', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('InterlockDevice_ID', models.CharField(choices=[('InterlockDevice_ID1', 'InterlockDevice_ID1'), ('InterlockDevice_ID2', 'InterlockDevice_ID2'), ('InterlockDevice_ID3', 'InterlockDevice_ID3'), ('InterlockDevice_ID4', 'InterlockDevice_ID4')], max_length=100)),
                ('Action_Taken', models.TextField()),
            ],
        ),
    ]
