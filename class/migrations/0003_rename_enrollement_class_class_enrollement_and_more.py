# Generated by Django 5.0.6 on 2024-06-23 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('class', '0002_rename_course_class_course'),
    ]

    operations = [
        migrations.RenameField(
            model_name='class',
            old_name='enrollement',
            new_name='class_enrollement',
        ),
        migrations.RenameField(
            model_name='class',
            old_name='teacher',
            new_name='class_teacher',
        ),
    ]
