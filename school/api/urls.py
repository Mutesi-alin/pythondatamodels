
from django.urls import path
from .views import StudentListView
from .views import ClassPeriodListView
from .views import ClassesListView
from .views import  CourseListView 
from .views import TeacherListView
from .views import StudentDetailView
from .views import ClassroomPeriodDetailView
from .views import TeacherDetailView
from .views import ClassDetailView
from .views import CourseDetailView

urlpatterns=[
    path("students/", StudentListView.as_view(), name="student_view"),
    path("periods/", ClassPeriodListView.as_view(), name="classroomPeriod_list_view"),
    path("classes/", ClassesListView.as_view(), name="classes_list_view"),
    path("courses/",  CourseListView .as_view(), name="courses_list_view"),
    path("teacher/",TeacherListView.as_view(), name="teacherslist_view"),
    
    path("students/<int:id>/" , StudentDetailView.as_view(),name= "student_detail_view"),
    path("periods/<int:id>/" , ClassroomPeriodDetailView.as_view(),name= "classroom_detail_view"),
    path("classes/<int:id>/" , ClassDetailView.as_view(), name="class"),
    path("courses/<int:id>/" , CourseDetailView.as_view(), name="course"),
    path("teacher/<int:id>/" , TeacherDetailView.as_view(), name="teachers"),
]




