# Generated by Django 4.0.3 on 2022-04-06 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=10)),
                ('mobile', models.IntegerField(max_length=10)),
                ('name', models.CharField(max_length=30)),
                ('event_time', models.CharField(max_length=30)),
                ('event_date', models.CharField(max_length=30)),
                ('event_location', models.CharField(max_length=30)),
                ('event_address', models.CharField(max_length=100)),
            ],
        ),
    ]
