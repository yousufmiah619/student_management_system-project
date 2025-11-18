from django.shortcuts import render
from .seralizers import TeacherSeralizer 
from .models import Teacher
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated , IsAdminUser
from django.contrib.auth import get_user_model

# Create your views here.
User=get_user_model()

@api_view(["GET","POST"])
@permission_classes([IsAuthenticated])
def teacher_list(request):
    if request.method == "GET" :
        course=Teacher.objects.all()
        seralizer=TeacherSeralizer(course, many=True)
        return Response(seralizer.data, status=200)

    if request.method == "POST":
        email=request.data.get("email")
        user_email=User.objects.filter(email=email).first()
        if user_email :
            return Response ({"message": "THis email already exit "},status=400)
        seralizer=TeacherSeralizer(data=request.data)
        if seralizer.is_valid():
            seralizer.save()
            contaxt={
                "message":"teacher added Successfully",
                "data":seralizer.data
            }
            return Response(seralizer.data ,status=201)
    return Response(seralizer.errors ,status=400)