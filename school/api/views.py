
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from student.models import Student
from .serializers import StudentSerializer

from  course.models import Course
from .serializers import CourseSerializer

from  classes.models import Classes
from .serializers import ClassesSerializer

from teacher.models import Teacher
from .serializers import TeacherSerializer

from ClassPeriod.models import ClassPeriod
from .serializers import ClassPeriodSerializer
from rest_framework import status


class StudentListView(APIView):
    def get (self,request):
        student = Student.objects.all()
        serializer =StudentSerializer(Student,many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StudentSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class  CourseListView(APIView):
    def get(self,request):
        courses= Course.objects.all()
        serializer = CourseSerializer(Course,many=True)
        return Response(serializer.data)
    
    
    def post(self, request):
        serializer = ClassesSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class TeacherListView(APIView):
    def get (self,request):
        teacher = Teacher.objects.all()
        serializer = TeacherSerializer(teacher,many=True)
        return Response(serializer.data)
    


    def post(self, request):
        serializer = TeacherSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class  ClassesListView (APIView):
    def get (self,request):
        classes = Classes.objects.all()
        serializer =   ClassesSerializer(classes,many=True)
        return Response(serializer.data)
    

    def post(self, request):
        serializer = ClassesSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ClassPeriodListView(APIView):
    def get (self,request):
        classperiod = ClassPeriod.objects.all()
        serializer = ClassPeriodSerializer(classperiod,many=True)
        return Response(serializer.data)


class StudentDetailView(APIView):
    def get (self, request,id):
        student = Student.objects.get(id = id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    def put (self, request,id):
        student = Student.objects.get(id = id)
        serializer = StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        student = Student.objects.get(id = id)
        student.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
class TeacherDetailView(APIView):
    def get (self, request,id):
        teacher = Teacher.objects.get(id = id)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)
    def put (self, request,id):
        teacher = Teacher.objects.get(id = id)
        serializer = TeacherSerializer(teacher,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        teacher = Teacher.objects.get(id = id)
        teacher.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
class ClassDetailView(APIView):
    def get (self, request,id):
        classes= Classes.objects.get(id = id)
        serializer = ClassesSerializer(classes)
        return Response(serializer.data)
    def put (self, request,id):
        classes = Classes.objects.get(id = id)
        serializer = StudentSerializer(classes,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        classes = Classes.objects.get(id = id)
        classes.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
class CourseDetailView(APIView):
    def get (self, request,id):
        course = Course.objects.get(id = id)
        serializer = CourseSerializer(course)
        return Response(serializer.data)
    def put (self, request,id):
        course = Course.objects.get(id = id)
        serializer = StudentSerializer(course,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        course = Student.objects.get(id = id)
        course.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    
class ClassroomPeriodDetailView(APIView):
    def get (self, request,id):
        classrom_period = ClassPeriod.objects.get(id = id)
        serializer = ClassPeriodSerializer(classrom_period)
        return Response(serializer.data)
    def put (self, request,id):
        classroom_period = ClassPeriod.objects.get(id = id)
        serializer = ClassPeriodSerializer(classroom_period,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        classroom_period = ClassPeriod.objects.get(id = id)
        classroom_period.delete()
        return Response(status=status.HTTP_202_ACCEPTED)



















