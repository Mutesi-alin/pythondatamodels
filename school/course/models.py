from django.db import models

# Create your models here.

from  teacher.models import Teacher
from classes.models import Classes

class Course(models.Model):
        course_name = models.CharField(max_length=100)
        course_id= models.CharField(max_length=10)
        course_description = models.TextField()
        course_ahead = models.PositiveSmallIntegerField()
        prerequisites = models.CharField(max_length=100)
        created_at= models.DateField()
        updated_at= models.DateField()
        trimester= models.PositiveSmallIntegerField()
        enrollment_limit= models.PositiveSmallIntegerField()
        teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name='courses')
        clas=  models.ManyToManyField(Classes, related_name='courses')
        




        def __str__(self):
            return f" {self.course_id} {self.course_name}"
