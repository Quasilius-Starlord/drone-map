# Generated by Django 3.2.9 on 2021-12-19 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DroneType',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('model_name', models.CharField(default='', max_length=40)),
                ('brand', models.CharField(default='', max_length=40)),
                ('model_year', models.CharField(max_length=10, null=True)),
                ('endurance_min', models.CharField(default='', max_length=20, null=True)),
                ('sl_no', models.CharField(default='', max_length=20, null=True)),
                ('type', models.CharField(default='', max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PilotData',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(default='', max_length=25, null=True)),
                ('address', models.CharField(default='', max_length=50, null=True)),
                ('phone', models.CharField(default='', max_length=15, null=True)),
                ('experience', models.IntegerField(default=0)),
                ('skill', models.IntegerField(default=0)),
                ('country', models.CharField(default='India', max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='DroneData',
            fields=[
                ('drone_name', models.CharField(default='', max_length=25, null=True)),
                ('reg_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('last_seen', models.DateTimeField(null=True)),
                ('first_launch', models.DateTimeField(null=True)),
                ('total_flight_time_min', models.IntegerField(default=0)),
                ('latitude', models.FloatField(default=0)),
                ('longitude', models.FloatField(default=0)),
                ('drone_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='api.dronetype')),
                ('pilot', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='api.pilotdata')),
            ],
        ),
    ]
