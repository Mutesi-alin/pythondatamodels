from django.db import models

class Student(models.Model):
    first_name= models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.EmailField()
    country= models.CharField(max_length=20)
    date_of_birth=models.DateField()
    code= models.PositiveSmallIntegerField()

    def __init__(self):
        return f" {self.first_name} {self.last_name}"
    



  
