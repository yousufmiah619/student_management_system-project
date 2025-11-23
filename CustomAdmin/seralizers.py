from rest_framework import serializers
from .models import Course, Subject

class CourseSeralizer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields="__all__"
        
class SubjectSeralizer(serializers.ModelSerializer):
    course=CourseSeralizer(read_only=True)
    course_id=serializers.PrimaryKeyRelatedField(source='course',
        queryset=Course.objects.all(),
        write_only=True
    )
    class Meta:
        model=Subject
        fields=["id","course","course_id","subject_name"]