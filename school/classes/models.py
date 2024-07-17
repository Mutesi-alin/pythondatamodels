from django.db import models
from teacher.models import Teacher

# Create your models here.

class Classes(models.Model):
        class_name = models.CharField(max_length=100)
        class_id = models.CharField(max_length=10)
        class_teacher = models.CharField(max_length=10)
        room_number = models.PositiveSmallIntegerField()
        class_speaciality= models.TextField()
        enrollement= models.TimeField()
        max_students = models.PositiveSmallIntegerField()
        academic_year = models.PositiveSmallIntegerField()
        capacity = models.PositiveSmallIntegerField()
        start_date= models.PositiveSmallIntegerField()
        end_date= models.PositiveSmallIntegerField()
        teacher= models.ForeignKey(Teacher,on_delete=models.SET_NULL, null=True, related_name='classa')
        


        def __str__(self):
            return f"{self.class_name} {self.class_id}"
