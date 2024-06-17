from django.db import models

class Course(models.Model):
        course_name = models.CharField(max_length=100)
        course_id= models.CharField(max_length=10)
        course_description = models.TextField()
        class_hours = models.PositiveSmallIntegerField()
        prerequisites = models.CharField(max_length=100)
        course_instructor =models.CharField(max_length=100)
        assessment_requirements = models.DateField()
        school_term =  models.PositiveSmallIntegerField()
        course_capacity =  models.PositiveSmallIntegerField()
        grade_level = models.PositiveSmallIntegerField()


        def __init__(self):
            return f" {self.course_id} {self.course_name}"
