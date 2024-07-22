# Generated by Django 5.0.6 on 2024-07-22 03:57

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_remove_course_course_instructor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='class_hours',
            new_name='course_ahead',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='assessment_requirements',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='course_capacity',
            new_name='enrollment_limit',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='grade_level',
            new_name='trimester',
        ),
        migrations.RemoveField(
            model_name='course',
            name='school_term',
        ),
        migrations.AddField(
            model_name='course',
            name='class_id',
            field=models.IntegerField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='teacher_id',
            field=models.IntegerField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='updated_at',
            field=models.DateField(default=22),
            preserve_default=False,
        ),
    ]