from django.urls import path
from .views import *

urlpatterns = [
    path('course-list/',course_list),
    path('subject-list/',subject_list)
]
