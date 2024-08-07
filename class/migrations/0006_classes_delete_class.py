# Generated by Django 5.0.6 on 2024-07-22 04:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class', '0005_remove_class_class_speciality_and_more'),
        ('teacher', '0003_rename_email_teacher_mail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=100)),
                ('class_id', models.CharField(max_length=10)),
                ('class_teacher', models.CharField(max_length=10)),
                ('room_number', models.PositiveSmallIntegerField()),
                ('class_speaciality', models.TextField()),
                ('enrollement', models.TimeField()),
                ('max_students', models.PositiveSmallIntegerField()),
                ('academic_year', models.PositiveSmallIntegerField()),
                ('capacity', models.PositiveSmallIntegerField()),
                ('start_date', models.PositiveSmallIntegerField()),
                ('end_date', models.PositiveSmallIntegerField()),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='classa', to='teacher.teacher')),
            ],
        ),
        migrations.DeleteModel(
            name='Class',
        ),
    ]
