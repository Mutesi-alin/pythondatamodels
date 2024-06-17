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
    


class Class(models.Model):
    class_name = models.CharField(max_length=100)
    class_id = models.CharField(max_length=10)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    room_number = models.PositiveSmallIntegerField()
    meeting_time = models.TimeField()
    enrollement= models.TimeField()
    max_students = models.PositiveSmallIntegerField()
    academic_year = models.PositiveSmallIntegerField()
    capacity = models.PositiveSmallIntegerField()
    Course= models.CharField(max_length=100)


    def __init__(self):
        return f" {self.class_name} {self.class_id}"

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_id= models.CharField(max_length=10)
    course_description = models.TextField()
    class_hours = models.PositiveSmallIntegerField()
    prerequisites = models.ManyToManyField('self', blank=True)
    course_instructor = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    assessment_requirements = models.DateField()
    school_term =  models.PositiveSmallIntegerField()
    course_capacity =  models.PositiveSmallIntegerField()
    grade_level = models.PositiveSmallIntegerField()


    def __init__(self):
        return f" {self.course_id} {self.course_name}"

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


    def __init__(self):
        return f" {self.first_name} {self.last_name}"