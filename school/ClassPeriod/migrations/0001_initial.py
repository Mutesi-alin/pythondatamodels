# Generated by Django 5.0.6 on 2024-07-16 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassPeriod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('classroom', models.CharField(max_length=23)),
                ('day_of_week', models.CharField(max_length=3)),
            ],
        ),
    ]
