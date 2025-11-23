from django.urls import path
from .views import *

urlpatterns = [
    path('add-student/',student_list),
    path('list-student/',student_list),
    path("student-details/<int:student_id>/",student_details)
]
