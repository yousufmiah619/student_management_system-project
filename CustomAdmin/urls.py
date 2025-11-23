from django.urls import path
from .views import *

urlpatterns = [
    path('course-list/',course_list),
    path('subject-list/',subject_list),
    path('course-details/<int:course_id>/',course_details),
    path('subject-details/<int:subject_id>/',subject_details)
]
