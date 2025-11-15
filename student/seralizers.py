from rest_framework import serializers
from .models import Student

class StudentSeralizer(serializers.ModelSerializer):
    class Meta:
        model=Student
        Fields="__all__"