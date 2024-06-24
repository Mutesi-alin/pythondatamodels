from django.db import models


class Course(models.Model):
        course_name = models.CharField(max_length=100)
        course_id= models.CharField(max_length=10)
        course_description = models.TextField()
        course_ahead = models.PositiveSmallIntegerField()
        prerequisites = models.CharField(max_length=100)
        teacher_id= 
        created_at= models.DateField()
        updated_at= models.DateField()
        trimester= models.PositiveSmallIntegerField()
        enrollment_limit= models.PositiveSmallIntegerField()
        class_id=




        def __str__(self):
            return f" {self.course_id} {self.course_name}"
