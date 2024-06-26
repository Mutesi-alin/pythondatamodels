# Generated by Django 5.0.6 on 2024-06-17 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=100)),
                ('class_id', models.CharField(max_length=10)),
                ('teacher', models.CharField(max_length=10)),
                ('room_number', models.PositiveSmallIntegerField()),
                ('meeting_time', models.TimeField()),
                ('enrollement', models.TimeField()),
                ('max_students', models.PositiveSmallIntegerField()),
                ('academic_year', models.PositiveSmallIntegerField()),
                ('capacity', models.PositiveSmallIntegerField()),
                ('Course', models.CharField(max_length=100)),
            ],
        ),
    ]
