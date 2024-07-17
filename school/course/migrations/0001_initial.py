# Generated by Django 5.0.6 on 2024-06-29 16:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('classes', '0001_initial'),
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
                ('course_id', models.CharField(max_length=10)),
                ('course_description', models.TextField()),
                ('course_ahead', models.PositiveSmallIntegerField()),
                ('prerequisites', models.CharField(max_length=100)),
                ('created_at', models.DateField()),
                ('updated_at', models.DateField()),
                ('trimester', models.PositiveSmallIntegerField()),
                ('enrollment_limit', models.PositiveSmallIntegerField()),
                ('clas', models.ManyToManyField(related_name='courses', to='classes.classes')),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='courses', to='teacher.teacher')),
            ],
        ),
    ]
