# Generated by Django 3.2.9 on 2021-12-14 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DroneData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drone_name', models.CharField(default='', max_length=25, null=True)),
                ('reg_id', models.IntegerField(default=0)),
                ('last_seen', models.DateTimeField(null=True)),
                ('first_launch', models.DateTimeField(null=True)),
                ('total_flight_time', models.IntegerField(default=0)),
                ('latitude', models.FloatField(default=0)),
                ('longitude', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='DroneType',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('model_name', models.CharField(default='', max_length=40)),
                ('brand', models.CharField(default='', max_length=40)),
                ('model_year', models.IntegerField(unique=True)),
                ('endurance_min', models.IntegerField(unique=True)),
                ('sl_no', models.CharField(default='', max_length=20)),
                ('type', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PilotData',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(default='', max_length=25, null=True)),
                ('address', models.CharField(default='', max_length=25, null=True)),
                ('phone', models.BigIntegerField(null=True)),
                ('experience', models.IntegerField(null=True)),
                ('skill', models.IntegerField(null=True)),
                ('country', models.CharField(default='', max_length=25, null=True)),
            ],
        ),
    ]