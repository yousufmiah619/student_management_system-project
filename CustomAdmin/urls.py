from django.urls import path
from .views import *

urlpatterns = [
    path('course_list/',course_list)
]
