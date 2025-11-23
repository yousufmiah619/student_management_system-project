from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Student 
from authentications.models import UserProfile 
from authentications.serializers import UserProfileSerializer
from CustomAdmin.seralizers import CourseSeralizer
from CustomAdmin.models import Course

User=get_user_model()

class StudentSeralizer(serializers.ModelSerializer):
    first_name = serializers.CharField(write_only=True)  # Remove name since it's not part of the User model
    last_name = serializers.CharField(write_only=True)  # Remove name since it's not part of the User model
    phone_number = serializers.CharField(write_only=True)
    email=serializers.EmailField(write_only=True)
    profile_picture = serializers.ImageField(write_only=True)
    course=CourseSeralizer(read_only=True)
    user=UserProfileSerializer(read_only=True)
    course_id=serializers.PrimaryKeyRelatedField(
        source='course',
        queryset=Course.objects.all(),
        write_only=True
    )
    class Meta:
        model = Student
        fields=["id","user","first_name","last_name","phone_number","email","profile_picture","roll_no","course","course_id"]
        
    def create(self, validated_data):   
        # Extract name from validated_data
        first_name = validated_data.pop('first_name')  # Remove name since it's not part of the User model
        last_name = validated_data.pop('last_name')  # Remove name since it's not part of the User model
        phone_number = validated_data.pop('phone_number')
        profile_picture = validated_data.pop('profile_picture')
        roll_no = validated_data.pop('roll_no')
        course = validated_data.pop('course')
        email = validated_data.pop('email')
        
        user = User.objects.create_user(
            email=email,
            password=roll_no ,
            role='student'
        )
        profile = UserProfile.objects.create(
            user=user,
            first_name=first_name,
            last_name = last_name,
            phone_number = phone_number,
            profile_picture = profile_picture,
        )
        student=Student.objects.create(user=profile , roll_no=roll_no , course=course)
        return student
    
    def update(self, instance, validated_data):
        user_data = validated_data.pop("user", None)

        if user_data:
            user = instance.user
            for field, value in user_data.items():
                setattr(user, field, value)
            user.save()

        for field, value in validated_data.items():
            setattr(instance, field, value)

        instance.save()
        return instance