from django.urls import path
from .views import  ClassPeriodListView 
from .views import StudentListView
from .views import  CourseListView
from .views import TeacherListView
from .views import ClassesListView 

urlpatterns = [
    path('classperiods/', ClassPeriodListView.as_view(), name='class_period_list'),
    path('courses/', CourseListView.as_view(), name='course_list'),
    path('classes/', ClassesListView.as_view(), name='classes_list'),
    path('teachers/', TeacherListView.as_view(), name='teacher_list'),
    path('students/', StudentListView.as_view(), name='student_list'),
]




