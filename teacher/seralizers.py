from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Teacher 
from authentications.models import UserProfile 
from authentications.serializers import UserProfileSerializer
from CustomAdmin.seralizers import CourseSeralizer
from CustomAdmin.models import Course
import random

def generate_otp():
    return str(random.randint(100000, 999999))  

User=get_user_model()

class TeacherSeralizer(serializers.ModelSerializer):
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
        model = Teacher
        fields=["id","user","first_name","last_name","phone_number","email","profile_picture","designation","course","course_id"]
        
    def create(self, validated_data):   
        # Extract name from validated_data
        first_name = validated_data.pop('first_name')  # Remove name since it's not part of the User model
        last_name = validated_data.pop('last_name')  # Remove name since it's not part of the User model
        phone_number = validated_data.pop('phone_number')
        profile_picture = validated_data.pop('profile_picture')
        designation = validated_data.pop('designation')
        course = validated_data.pop('course')
        email = validated_data.pop('email')
        password=generate_otp()
        user = User.objects.create_user(
            email=email,
            password=password ,# Use roll_no as password (convert to string)
            role='teacher' # Set default role
        )
        # user = User.objects.create_user(
        #     email=validated_data['email'],
        #     password=validated_data['roll_no'],
        #     role=validated_data.get('role' , 'student')
        # )
        profile = UserProfile.objects.create(
            user=user,
            first_name=first_name,
            last_name = last_name,
            phone_number = phone_number,
            profile_picture = profile_picture,
        )
        # Subscription.objects.create(user=user)
        teacher=Teacher.objects.create(user=profile , designation=designation , course=course)
        return teacher
    
