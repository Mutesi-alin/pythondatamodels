from django.db import models


class Class(models.Model):
        class_name = models.CharField(max_length=100)
        class_id = models.CharField(max_length=10)
        class_teacher = models.CharField(max_length=10)
        room_number = models.PositiveSmallIntegerField()
        class_speaciality= models.TextField()
        class_enrollement= models.TimeField()
        max_students = models.PositiveSmallIntegerField()
        academic_year = models.PositiveSmallIntegerField()
        capacity = models.PositiveSmallIntegerField()
        start_date= models.PositiveSmallIntegerField()
        end_date= models.PositiveSmallIntegerField()
        


        def __str__(self):
            return f"{self.class_name} {self.class_id}"
        
