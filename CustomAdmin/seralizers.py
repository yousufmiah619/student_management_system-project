from rest_framework import serializers
from .models import Course, Subjct

class CourseSeralizer(serializers.ModelSerializer):
    class Meta:
        model=Course
        Fields="__all__"
        
class SubjectSeralizer(serializers.ModelSerializer):
    class Meta:
        model=Subjct
        Fields="__all__"