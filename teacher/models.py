from django.db import models

# Create your models here.
class Teacher(models.Model):
        first_name = models.CharField(max_length=100)
        last_name = models.CharField(max_length=100)
        nationality = models.CharField(max_length=50)
        department = models.CharField(max_length=100)
        email = models.EmailField()
        course = models.CharField(max_length=100)
        teacher_id = models.PositiveSmallIntegerField()
        bank_account_number = models.CharField(max_length=50)
        date_of_joining = models.DateField()
        gender = models.CharField(max_length=7)


        def __str__(self):
            return f" {self.first_name} {self.last_name}"