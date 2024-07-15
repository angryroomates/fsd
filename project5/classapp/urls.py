from django.urls import path
from . import views

urlpatterns=[
    path('',views.courses_list,name="courses_list"),
    path('<int:course_id>/',views.course_details,name="course_details"),
    path('<int:course_id>/register',views.student_register,name="student_register"),
]