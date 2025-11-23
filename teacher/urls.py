from django.urls import path
from .views import *

urlpatterns = [
    path('add-teacher/',teacher_list),
    path("list-teacher/",teacher_list),
    path("teacher-details/<int:teacher_id>/",teacher_details)
]
