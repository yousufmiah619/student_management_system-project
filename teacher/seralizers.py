from rest_framework import serializers
from .models import Teacher

class TeacherSeralizer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        Fields="__all__"